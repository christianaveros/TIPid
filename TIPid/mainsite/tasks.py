# Create your tasks here
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
	jsondata = json.loads(soup.find('script', text=re.compile	(r'window.pageData=')).get_text().replace('window.pageData=', ''))
	return jsondata

@shared_task
def scraper_shopee(search_term):
	browser = webdriver.Chrome()
	browser.get('https://shopee.ph/search/?is_official_shop=1&keyword=' + search_term + '&page=0')
	soup = BeautifulSoup(browser.page_source)
	items = soup.find_all(class_="shopee-search-result-view__item-card")
	item_list = []
	"""
	for item in items:
		item.append{
			'name': item.find(class_=""),
			'price': item.find(class_="", text=re.compile(r'₱(...)+₱|,|₱')),
			'rating': item.find_all(class_=""),
			'reviews': item.find(class_="")
		}
	"""
