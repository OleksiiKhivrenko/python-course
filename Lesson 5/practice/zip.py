# функция берёт на вход несколько списков и создаёт из них список (в Python 3 создаётся не list, а специальный
# zip-объект) кортежей, такой, что первый элемент полученного списка содержит кортеж из первых элементов всех
# списков-аргументов. Таким образом, если ей передать три списка, то она отработает следующим образом:
from itertools import zip_longest

s = 'abc'
t = (10, 20, 30)

print(list(zip(s, t)))
# [('a', 10), ('b', 20), ('c', 30)]

s = 'abc'
t = (10, 20, 30)
u = (-5, -10, -15)

print(list(zip(s, t, u)))
# [('a', 10, -5), ('b', 20, -10), ('c', 30, -15)]

names = ['Tom', 'Dick', 'Harry']
ages = [50, 35, 60]

print(dict(zip(names, ages)))
# {'Harry': 60, 'Dick': 35, 'Tom': 50}

s = 'abc'
t = (10, 20, 30, 40)
print(list(zip(s, t)))
print(list(zip_longest(s, t)))
# [('a', 10), ('b', 20), ('c', 30)]
# [('a', 10), ('b', 20), ('c', 30), (None, 40)]
