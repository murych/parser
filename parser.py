
# -*- encoding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
import codecs
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Beautifulsoup docs

def get_authors_and_titles_by_class( target_url, container_tag, container_attrs, title_tag, title_class ):
    r = requests.get(target_url)  # assign the response to a variable r
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,  "html.parser")
    container = soup.find(container_tag, attrs=container_attrs)
    top_titles = container.find_all(title_tag,class_=title_class)
    return top_titles
    

target_urls = ["http://www.livelib.ru/books/top", "http://readrate.com/rus/ratings/top100"]

top_by_sites = {} # { site url : (titles) }

for url in target_urls:
    if 'readrate' in url:
       title_tag= 'div'
       title_class = "title"
       container_tag = 'div'
       container_attrs = {'class': "books-list"}
    elif 'livelib' in url:
        title_tag = 'a', 'a'
        title_class = "tag-book-title"
        container_tag = 'table'
        container_attrs = {'class': "linear-list"}


    top_by_sites[url] = get_authors_and_titles_by_class(url, container_tag, container_attrs, title_tag, title_class)

parse_result = Livelub.parse()

class Site():
    link = None

class Livelib():
    link = "http://www.livelib.ru/books/top"
    def parse():
        return Livelib.get_titles()


    def get_titles():
        return []

class IterLib():
   def parse():
        return IterLib.get_titles()


    def get_titles():
        return []
        
with codecs.open('output.txt','w',encoding='utf-8') as f:
    for key in list(top_by_sites.keys()):
        f.write(u'\n%s\n\n'%(key))
        for i in range(len(top_by_sites[key])):
            f.write(u'%s\n'%(top_by_sites[key][i].text))