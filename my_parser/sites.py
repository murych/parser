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
		self.title_tag = 'a'
		self.title_attrs = {'class': "tag-book-title"}
		self.container_tag = 'table'
		self.container_attrs = {'class': "linear-list"}
		self.authors_tag = 'a'
		self.authors_attrs = {'class': 'tag-book-author'}

class ReadRate(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag= 'div'
		self.title_attrs = {'class': "title"}
		self.container_tag = 'div'
		self.container_attrs = {'class': "books-list"}
		self.authors_tag = 'li'
		self.authors_attrs = {'class': 'contributor item'}

class Libs(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag = 'h2'
		self.title_attrs = {}
		self.container_tag = 'div'
		self.container_attrs = {'class': "posts doocode_book_result_filter"}
		self.authors_tag = 'div'
		self.authors_attrs = {'class': 'uk-width-10-10 uk-width-medium-5-10  uk-width-large-5-10'}

	def get_top(self):
		top_titles, top_authors = Site.get_top(self)
		# Нет определленого у тега с авторами нет определенного класса
		# Используется другой способ поиска
		top_libs_authors = []
		for i in top_authors:
			author = i.find('a')
			if author != None:
				top_libs_authors.append(author)
		# (Костыль) У книги на 25 месте нету автора
		top_libs_authors.insert(24,"Неизвестный автор")
		return top_titles, top_libs_authors