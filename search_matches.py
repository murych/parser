import codecs
import re, copy

# Записываем данные из файла в словарь
def open_file(file_name):
    f = codecs.open(file_name, 'r','utf-8')
    key = ''
    for line in f:
        if line != '\r\n':
            # Если в строке есть имя сайта то создаем словарь с ключем, являющимся именем сайта
            if (re.findall('(\w+\.\w+)\:', line)):
                if len(list_of_book) != 0:
                    # Под этот ключ записываем список книг
                    dict_of_book[key] = copy.copy(list_of_book)
                    # Очищаем список книг
                    del list_of_book[:]
                # Задаем новый ключ со следующим сайтом
                key = re.findall('(\w+\.\w+)\:', line)[0]
            else:
                # Из строки с номером, названием и автором выбираем только названи е книги
                book_name = re.findall('\d+\) (.+) \-', line)[0]
                list_of_book.append(book_name)
    if len(list_of_book) != 0:
        dict_of_book[key] = list_of_book

# Проходимся по полученному словарю и сравниваем список книг каждого сайта с каждым другим сайтом
def find_match(book):
    list_of_key =[]
    for key in dict_of_book:
        list_of_key.append(key)
    for i in range(len(list_of_key)):
        j = i + 1
        key1 = list_of_key[i]
        while(j <= len(list_of_key)-1):
            key2 = list_of_key[j]
            for n in range(100):
                if (dict_of_book[key1][n] == dict_of_book[key2][n]):
                    print('%d - %s - %s / %s'%(n+1,dict_of_book[key1][n],key1,key2))
            j += 1

dict_of_book = {}
list_of_book = []
open_file("out.txt")
find_match(dict_of_book)
