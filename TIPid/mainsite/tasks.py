# Create your tasks here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from bs4 import BeautifulSoup
import json
import requests
import re
from selenium import webdriver
from mainsite.models import Item

"""
	
	DOWNLOAD CHROMEDRIVER, EXTRACT, COPY TO /usr/bin/
	RUN IN SEPARATE PANE:
	$ celery -A config worker -l info
	
	ADD THESE IN VIEWS.PY
	from mainsite.tasks import *
	
	...

	array = scraper_lazada.add_async(search_term).get() //returns array of dict from osw
	
"""
@shared_task
def scrapers(search_term):
	item_list = []
	try:
		lazada = scraper_lazada(search_term)
		shopee = scraper_shopee(search_term)
		amazon = scraper_amazon(search_term)
		item_list = [item for item in lazada[0:20]]
		item_list += [item for item in shopee[0:20]]
		item_list += [item for item in amazon[0:20]]
		item = Item.objects.create_item(search_term, item_list)
	except Exception as e:
		item_list = [{'Error': 'An error occured:' + str(e)}]
		raise e


	return item.id

@shared_task
def scraper_lazada(search_term):
	url = 'https://www.lazada.com.ph/catalog/?q=' + search_term
	data = requests.get(url).text
	soup = BeautifulSoup(data, 'html.parser')
	jsondata = json.loads(soup.find('script', text=re.compile(r'window.pageData=')).get_text().replace('window.pageData=', ''))
	items = jsondata['mods']['listItems']
	item_list = []
	for item in items[0:20]:
		rating = float(item['ratingScore'])
		reviews = float(item['review'])
		bayes_est = (5 * 3 + rating * reviews)/(5 + reviews)
		item_list.append({
			'name': item['name'], 
			'website': 'lazada',
			'url': item['productUrl'],
			'price': item['price'],
			'rating': rating,
			'reviews': int(reviews),
			'bayes_est': bayes_est
			})
	return item_list

@shared_task
def scraper_shopee(search_term):
	browser = webdriver.Chrome()
	browser.get('https://shopee.ph/search/?is_official_shop=1&keyword=' + search_term + '&page=0')
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	items = soup.find_all(class_="shopee-search-result-view__item-card")
	browser.close()
	item_list = []

	for item in items:
		# price = float(item.find(class_="shopee-item-card__current-price").text.replace('₱','').replace(',',''))
		rating = float(len(item.find_all(class_="shopee-rating-stars__lit", style=re.compile('100%'))))
		price = re.sub(r'(\₱|,|\s-.*)', '', item.find(class_="shopee-item-card__current-price").text)
		try:
			reviews = float(item.find(class_="shopee-item-card__btn-ratings-count").text.replace('(', '').replace(')', ''))
		except ValueError:
			reviews = 0
		bayes_est = (5 * 3 + rating * reviews)/(5 + reviews)
		item_list.append({
			'name': item.find(class_="shopee-item-card__text-name").text, 
			'website': 'shopee',
			'url': 'https://shopee.ph' + item.find(class_="shopee-item-card--link")['href'],
			'price': float(price),
			'rating': rating,
			'reviews': int(reviews),
			'bayes_est': bayes_est	
				})
	return item_list

@shared_task
def scraper_amazon(search_term):
	item_list = []
	for i in range(1,3):
		browser = webdriver.Chrome()
		browser.get('https://www.amazon.com/s/field-keywords=' + search_term + '&page=' + str(i))
		soup = BeautifulSoup(browser.page_source, 'html.parser')
		browser.close()
		items = soup.find_all(id=re.compile('result_'))
		for item in items:
			if((item.find(class_=re.compile('s-access-title'))) and (str(item.find(class_=re.compile('a-offscreen')))!='<span class="a-offscreen">[Sponsored]</span>') and (item.find(class_=re.compile('a-offscreen')) is not None)) :
				if item.find(href=re.compile('#customerReviews')) is not None:
					rating = float(item.find(class_=re.compile('a-icon-star')).text.replace(' out of 5 stars', ''))
					reviews = float(item.find(href=re.compile('#customerReviews')).text.replace(',', ''))
				else:
					rating = reviews = 0
				price = re.sub(r'(\$|,|\s-.*)', '', item.find(class_=re.compile('a-offscreen')).text)
				bayes_est = (5 * 3 + rating * reviews)/(5 + reviews)
				item_list.append({
					'name': item.find(class_=re.compile('s-access-title')).text,
					'website': 'amazon', 
					'url': item.find(class_=re.compile('s-access-detail-page'))['href'], 
					'price': float(price)*50,
					'rating': rating,
					'reviews': int(reviews),
					'bayes_est': bayes_est 
					})
	return item_list
