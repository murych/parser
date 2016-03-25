# -*- coding: utf-8 -*-
from sites import *


def save_file(topsites):
	with open("out.txt", "w", encoding="utf-8") as f:
		for site in topsites:
			f.write(u'\nТоп 100 книг по версии сайта %s:\n\n' % (site.name))
			top = site.get_top()
			for i in range(len(top[0])):
				try:
					f.write(u'%d) %s - %s\n' % (i + 1, top[0][i].text, top[1][i].text))
				except AttributeError:
					f.write(u'%d) %s - Неизвестный автор\n' % (i + 1,top[0][i].text))

livelib = LiveLib('http://www.livelib.ru/books/top')
readrate = ReadRate('http://readrate.com/rus/ratings/top100')
libs = Libs('http://libs.ru/best-100')

save_file([livelib, readrate, libs])
