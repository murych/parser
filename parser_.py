import re
import codecs
import requests
from bs4 import BeautifulSoup


def write_file(name, url, top_title):
        with codecs.open('%s.txt' % name, 'w', encoding='utf-8') as f:
            f.write(u'%s\n%s\n\n' % (name, url))
            for title in top_title:
                f.write('%s\n' % title)


class Site():
    def __init__(self, url):
        self.url = url
        self.name = re.match('^(?:http?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)', url).group(1)

    def parse(self):
        r = requests.get(self.url)
        r.encoding = 'utf-8'
        return BeautifulSoup(r.text, 'html.parser')

    def get_top(self):
        soup = self.parse()
        container = soup.find(self.container_tag, attrs=self.container_attrs)
        top_title = container.find_all(self.title_tag, self.title_attrs)
        top_title = list(map(lambda title: title.text, top_title))
        return top_title


class LiveLib(Site):
    def __init__(self, url):
        Site.__init__(self, url)
        self.title_tag, self.title_attrs = 'a', {'class': 'tag-book-title'}
        self.container_tag, self.container_attrs = 'table', {'class': 'linear-list'}


class ReadRate(Site):
    def __init__(self, url):
        Site.__init__(self, url)
        self.title_tag, self.title_attrs = 'div', {'class': 'title'}
        self.container_tag, self.container_attrs = 'div', {'class': 'books-list'}

livelib = LiveLib('http://www.livelib.ru/books/top')
readrate = ReadRate('http://readrate.com/rus/ratings/top100')

write_file(livelib.name, livelib.url, livelib.get_top())
write_file(readrate.name, readrate.url, readrate.get_top())
