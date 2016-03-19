#pip install beautifulsoup4
#pip install requests

# -*- encoding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Beautifulsoup docs
#http://docs.python-requests.org/en/master/
#Requests docs


#target_urls = ["http://www.livelib.ru/books/top", "http://readrate.com/rus/ratings/top100"]
target_url = "http://www.livelib.ru/books/top"
r = requests.get(target_url)  # assign the response to a variable r


r.encoding = 'utf-8'

soup = BeautifulSoup(r.text,  "html.parser")
top_titles = soup.find_all("a",class_="tag-book-title")

with open('output.txt','w',encoding='utf-8') as f:
    for i in range(len(top_titles)):
        f.write('%s\n'%(top_titles[i].text))