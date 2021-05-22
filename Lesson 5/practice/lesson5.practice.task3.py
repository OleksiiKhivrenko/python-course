# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись

# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!

import re
import sys


def count_words(word, dict_words):
    if word.lower() in dict_words:
        dict_words[word] += 1
    else:
        dict_words[word] = 1


def calc_words(text):
    words_list = list(re.findall(r'\w+', text))
    dict_total = dict()
    list(map(lambda word: count_words(word, dict_total), words_list))
    return dict_total


filename = sys.argv[0]
# далее открываем файл на чтение (опция 'r')
f = open("task3.txt", 'r')  # в файле теперь file descriptor

file_lines = f.readlines()
file_text = "".join(file_lines)

words_total = calc_words(file_text)
print(words_total)

f.close()  # закрытие файла
