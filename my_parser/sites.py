import requests
import re
from bs4 import BeautifulSoup

class Site():
	def __init__(self, url):
		self.url = url
		# Из полного адреса выбираем имя.домен
		self.name = re.findall('(\w+\.\w+)\/', url)[0]
	
	def parse(self):
		r = requests.get(self.url)
		r.encoding = 'utf-8'
		return BeautifulSoup(r.text, 'html.parser')

	def get_top(self):
		soup = self.parse()
		container = soup.find(self.container_tag, attrs=self.container_attrs)
		top_titles = container.find_all(self.title_tag, attrs=self.title_attrs)
		top_authors = container.find_all(self.authors_tag, attrs=self.authors_attrs)
		return top_titles, top_authors

class LiveLib(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag, self.title_attrs = 'a', {'class': "tag-book-title"}
		self.authors_tag, self.authors_attrs = 'a', {'class': 'tag-book-author'}
		self.container_tag, self.container_attrs = 'table', {'class': "linear-list"}

class ReadRate(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag, self.title_attrs= 'div', {'class': "title"}
		self.authors_tag, self.authors_attrs = 'li', {'class': 'contributor item'}
		self.container_tag, self.container_attrs = 'div', {'class': "books-list"}

class Libs(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag, self.title_attrs = 'h2', {}
		self.authors_tag, self.authors_attrs = 'a', {'class': re.compile('/a/')}
		self.container_tag, self.container_attrs = 'div', {'class': "posts doocode_book_result_filter"}
