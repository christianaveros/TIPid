from bs4 import Beautiful Soup
import json
import requests
import re

def lazadascraper(search_term):
	url = 'https://www.lazada.com.ph/catalog/?q=' + search_term
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
jsondata = json.loads(soup.find('script', text=re.compile(r'window.pageData=')).get_text().replace('window.pageData=', ''))
