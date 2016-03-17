import re

urls = {'livelib': 'http://www.livelib.ru/books/top',
		'readrate': 'http://readrate.com/rus/ratings/top100',
		'readly': 'http://readly.ru/books/top/'}


def params(url):
	if 'readrate' in url:
		title_tag = 'div'
		title_attrs = {'class': 'title'}
		author_tag = 'a'
		author_attrs = {'href': re.compile('contributor')}
		container_tag = 'div'
		container_attrs = {'class': 'books-list'}
	elif 'livelib' in url:
		title_tag = 'a'
		title_attrs = {'class': 'tag-book-title'}
		author_tag = 'a'
		author_attrs = {'class': 'tag-book-author'}
		container_tag = 'table'
		container_attrs = {'class': 'linear-list'}
	elif 'readly' in url:
		title_tag = 'h3'
		title_attrs = {'class': 'blvi__title'}
		author_tag = 'a'
		author_attrs = {'href': re.compile('author')}
		container_tag = 'div'
		container_attrs = {'class': 'book-list-view'}
	return container_tag, container_attrs, title_tag, title_attrs, author_tag, author_attrs
