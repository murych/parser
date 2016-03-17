'''
NOTE: если названия книг будут различаться хотя бы на одну букву,
алгоритм не прожует :с
'''

import codecs
from params_ import urls

get_top = lambda name: list(map(lambda line: line.rstrip('\n'),
                                codecs.open('%s.txt' % (name),
                                'r', 'utf-8')))[3:18]

if __name__ == '__main__':
    with codecs.open('compare.txt', 'w', 'utf-8') as f:
        tops = list(map(lambda name: list(zip(get_top(name))),
                        list(urls.keys())))
        for i in range(len(tops[0])):
            if tops[0][i] == tops[1][i]:
                f.write('%d - %s - %s|%s' % (i + 1, tops[0][i][0],
                                             urls['livelib'], urls['readly']))
            elif tops[1][i] == tops[2][i]:
                f.write('%d - %s - %s|%s' % (i + 1, tops[1][i][0],
                                             urls['readly'], urls['readrate']))
            elif tops[0][i] == tops[2][i]:
                f.write('%d - %s - %s|%s' % (i + 1, tops[0][i][0],
                                             urls['livelib'], urls['readrate']))
