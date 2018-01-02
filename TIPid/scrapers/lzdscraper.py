from bs4 import BeautifulSoup
from .models import LazadaProductResponses
import json
import requests
import re
from selenium import webdriver

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

def scraper_lzd(search_term):
	url = 'https://www.lazada.com.ph/catalog/?q=' + search_term
	data = requests.get(url).text
	soup = BeautifulSoup(data, 'html.parser')
	string_data = soup.find('script', text=re.compile(r'window.pageData=')).get_text().replace('window.pageData=', '')
	json_data = json.loads(string_data)
	item_list = json_data['mods']['listItems']


