import codecs
import requests
from bs4 import BeautifulSoup
from params_ import urls, params


def get_top(url):
    container_tag, container_attrs, title_tag, title_attrs,\
        author_tag, author_attrs = params(url)
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    container = soup.find(container_tag, attrs=container_attrs)
    return list(map(lambda div: div.text, container.find_all(title_tag, title_attrs))),\
        list(map(lambda div: div.text, container.find_all(author_tag, author_attrs)))


def parse(name):
    top_title, top_author = get_top(urls[name])
    with codecs.open('%s.txt' % name, 'w', encoding='utf-8') as f:
        f.write(u'%s\n%s\n\n' % (name, urls[name]))
        for title, author in zip(top_title, top_author):
            f.write(u'%s - %s\n' % (' '.join(author.strip('\n').split()),
                                    title.strip('\n')))

if __name__ == '__main__':
    for name in urls.keys():
        parse(name)
