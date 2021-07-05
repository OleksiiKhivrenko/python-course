# Заканчиваем прошлые задачи, украшаем работу физбазов работой со строками, списками, пробуем генераторы списков и
# прочие новые красоты, которые выучили. Доводим код до идеала!

s = "string"
f = 1.23423432

print('%s %.2f' % (s, f))

s = "Information {d} people!"
print(s.format(**{"d": 3}))

l2 = [x * x for x in range(1, 11)]
print(l2)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = [str(elem) for elem in my_list if (not elem % 3)]
print(l1)

list_2 = [1, 2, 3, 4, 5]
list_3 = list_2[:len(list_2)]

list_2.append(2)

print(list_2, list_3)

# Создание строк, кавычки

S1 = 'Welcome to strings'
S2 = "Another string"
S3 = """And '''another'''
long
string"""
S4 = 'This "string" is a bit """crazy"""'

# Простые операции

S = 'abc'
print(len(S))  # Выведет 3
S = S + '12'  # В S будет 'abc12'
print(S[2])  # Выведет 'c'
print('ab' * 2)  # Выведет abab

# Строка - неизменяемый тип

str1 = 'asdfghj'
# str1[5] = 's'
# Python ругается, строки такую операцию не поддерживают. Ок...
str1 = str1[:5] + 's' + str1[6:]

# Срезы строк

s = "Welcome to California!"
print(s)
print(s[:5])
print(s[:])
print(s[:-3])
print(s[::-1])
print(s[:5:2])

# Полезные функции работы со строками
print("\n")
print(len(s))  # получить длину строки
print(s.find('C'))  # найти индекс начала первой подстроки в строке
print(s.replace('C', '7'))  # Заменяет все подстроки на новые
print(s.split())  # Разбивает строку по разделителю и создает список. По умолчанию разделитель - пробел
print(s.upper())
S += '\n\n'
print(S)
print(S.rstrip())  # удаление пробельных символов в конце

# Форматирование строк
print("\n")
S = 'Welcome to'
C = 'Ukraine!'
print(S + ' ' + C)

# Форматирование с оператором %
print("\n")
S = 'Welcome to'
C = 'Ukraine!'
print('%s %s' % (S, C))

C = 'Ukraine'
S = 'welcomed'
print('%d people are %s in %s!' % (3, S, C))

# Форматирование с оператором % с использованием словаря
D = {'country': 'Ukraine', 'greetings': 'welcomed', 'pretext': 'in', 'number': 3}
S = "Information! %(number)d people are %(greetings)s %(pretext)s %(country)s!"
print(S % D)
# Information! 3 people are welcomed in Ukraine!

# Форматирование при помощи метода .format()
# подставляя переменные по порядку с указанием позиции
# подставляя переменные по порядку без указания позиции
# подставляя переменные по названию
# в смешанном стиле
# Работает это так. Укажем позиции подставляемых значений порядку от нуля:

S = "Information! {3} people are {1} {2} {0}!"

print(S.format(3, 'welcomed', 'in', 'Ukraine'))
# Аналогичный пример, но укажем позиции подставляемых значений порядку без укзаания позиции:

S = "Information! {} people are {} {} {}!"
print(S.format(3, 'welcomed', 'in', 'Ukraine'))
# Аналогичный пример, но укажем позиции подставляемых значений порядку без укзаания позиции:

S = "Information! {} people are {} {} {}!"
S.format(3, 'welcomed', 'in', 'Ukraine')
print(S.format(3, 'welcomed', 'in', 'Ukraine'))
# 'Information! 3 people are welcomed in Ukraine!'


# List (список)
print("\n")

# пустой список
empty_list = []
# Простое перечисление:
a = [2, 2.25, "Python"]

# Преобразуем строку в список
b = list("help")
# ['h', 'e', 'l', 'p']

b = 'welcome to the hell'.split()
# ['welcome', 'to', 'the', 'hell']


# Некоторые функции работы со списками
# Ниже представлены примеры работы некоторых функций работы со списками:

L = list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L.append(12)  # Добавляет элемент в конец списка
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
L.extend([13, 14])  # Добавляет элементы второго списка в конец первого
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
L.insert(2, 5)  # Вставляет на второе место цифру 5
# [1, 2, 5, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
L.remove(5)  # Удаляет первую встретившуюся пятерку
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]

print(L)

L = list(map(str, range(1, 11)))
print(L)
# L
# # функция map применяет переданную ей функцию к списку

S = ': '.join(L)  # склеивает строки в списке в одну, вызывается от разделителя
print(S)

# Циклы и списки
# Цикл for специально создан для того, чтобы выполнять повторяющиеся действия со списками и другими итерируемыми объектами. Пара примеров:
#
S = 'This is Sparta!!'
L = S.split()

for num, elem in enumerate(L):
    print(str(num) + '. say ' + elem)

l = []
for x in range(1, 11):
    l.append(x * x)

print(l)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# то же самое с list comprehension
l2 = [x * x for x in range(1, 11)]
print(l2)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# result_list = [actions_with_var for var in list if condition]
