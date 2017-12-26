# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from bs4 import BeautifulSoup
import json
import requests
import re

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
