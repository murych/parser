import codecs
import requests
from bs4 import BeautifulSoup
from params_ import urls, params


def get_top(url):
	container_tag, container_attrs, title_tag, title_attrs,\
		author_tag, author_attrs = params(url)  # вызов функции из params_.py
	r = requests.get(url)
	r.encoding = 'utf-8'
	soup = BeautifulSoup(r.text, "html.parser")
	container = soup.find(container_tag, attrs=container_attrs)
	top_title = container.find_all(title_tag, class_=title_attrs)
	top_author = container.find_all(author_tag, class_=author_attrs)
	return top_title, top_author


def parse(name):
	top_title, top_author = get_top(urls[name])
	with codecs.open('%s.txt' % name, 'w', encoding='utf-8') as f:
		f.write(u'%s\n%s\n\n' % (name, urls[name]))
		for title, author in zip(top_title, top_author):
			# итерируем по двум спискам одновременно
			f.write(u'%s - %s\n' % (' '.join(author.strip('\n').split()).text,
                           title.strip('\n')).text)

if __name__ == '__main__':
    for name in urls.keys():
        parse(name)
