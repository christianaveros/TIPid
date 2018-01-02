# Create your tasks here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from bs4 import BeautifulSoup
import json
import requests
import re
from selenium import webdriver

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def scrapers(search_term):
	url = 'https://www.lazada.com.ph/catalog/?q=' + search_term
	data = requests.get(url).text
	soup = BeautifulSoup(data, 'html.parser')
	jsondata = json.loads(soup.find('script', text=re.compile(r'window.pageData=')).get_text().replace('window.pageData=', ''))
	items = jsondata['mods']['listItems']
	item_list = []
	for item in items[0:19]:
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
	item_list = []

	for item in items:
		rating = float(len(item.find_all(class_="shopee-rating-stars__lit", style=re.compile('100%'))))
		try:
			reviews = float(item.find(class_="shopee-item-card__btn-ratings-count").text.replace('(', '').replace(')', ''))
		except ValueError:
			reviews = 0
		bayes_est = (5 * 3 + rating * reviews)/(5 + reviews)
		item_list.append({
			'name': item.find(class_="shopee-item-card__text-name").text, 
			'website': 'shopee',
			'url': item.find(class_="shopee-item-card--link")['href'],
			'price': float(item.find(class_="shopee-item-card__current-price").text.encode('utf-8').replace('\xe2\x82\xb1','').replace(',','')),
			'rating': rating,
			'reviews': int(reviews),
			'bayes_est': bayes_est	
				})
	return item_list


	"""

@shared_task
def scraper_amazon(search_term):
	item_list = []
	for i in range(1,3):
		browser = webdriver.Chrome()
		browser.get('https://www.amazon.com/s/field-keywords=' + search_term + '&page=' + str(i))
		soup = BeautifulSoup(browser.page_source, 'html.parser')
		items = soup.find_all(class_="s-result-item celwidget ")

		for item in items[2:]:
			if(item.find(class_=re.compile('s-access-title'))):
				rating = float(item.find(class_=re.compile('a-icon-star')).text.replace(' out of 5 stars', ''))
				reviews = float(item.find(href=re.compile('#customerReviews')).text.replace(',', ''))
				bayes_est = (5 * 3 + rating * reviews)/(5 + reviews)
				item_list.append({ 'name': item.find(class_=re.compile('s-access-title')).text, 'website': 'amazon', 'url': item.find(class_=re.compile('s-access-detail-page'))['href'], 'price': float(item.find(class_=re.compile('a-offscreen')).text.replace('$', ''))*50, 'rating': rating, 'reviews': int(reviews), 'bayes_est': bayes_est })

	return item_list

	"""