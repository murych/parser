import codecs
from params_ import *


def write_file(name, url, top_title):
		with codecs.open('%s.txt' % name, 'w', encoding='utf-8') as f:
			f.write(u'%s\n%s\n\n' % (name, url))
			for title in top_title:
				f.write('%s\n' % title.strip('\n'))

livelib = LiveLib('http://www.livelib.ru/books/top')
readrate = ReadRate('http://readrate.com/rus/ratings/top100')
readly = Readly('http://readly.ru/books/top')

write_file(livelib.name, livelib.url, livelib.get_top())
write_file(readrate.name, readrate.url, readrate.get_top())
write_file(readly.name, readly.url, readly.get_top())
