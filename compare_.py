'''
NOTE: если названия книг будут различаться хотя бы на одну букву,
алгоритм не прожует :с
'''
import codecs
from params_ import urls


def get_top(name):
	'''
	собираем все файлы с топами в один список
	каждая ячейка - список топа одного сайта, вида
	[[readly], [readrate], [livelib]]
	'''
	top = list(codecs.open('%s.txt' % (name), 'r', 'utf-8'))[3:18]
	for line in top:
		line = line.rstrip('\n')
	return top

if __name__ == '__main__':
	with codecs.open('compare.txt', 'w', 'utf-8') as f:
		tops = []
		for name in list(urls.keys()):
			tops.append(list(zip(get_top(name))))
		for i in range(len(tops[0])):
			if tops[0][i] == tops[1][i]:
				f.write('%d - %s - %s|%s' % (i+1, tops[0][i][0],
											 urls['livelib'], urls['readly']))
			elif tops[1][i] == tops[2][i]:
				f.write('%d - %s - %s|%s' % (i+1, tops[1][i][0],
											 urls['readly'], urls['readrate']))
			elif tops[0][i] == tops[2][i]:
				f.write('%d - %s - %s|%s' % (i+1, tops[0][i][0],
											 urls['livelib'], urls['readrate']))
