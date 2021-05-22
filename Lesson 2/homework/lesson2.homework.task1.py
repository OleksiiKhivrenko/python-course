# if -> elif -> else

print("Give it to me!")
number = int(input())

if number >= 100:
    print("Thanks, man!")
elif (number > 10) and (number < 100):
    print("OK :(")
else:
    print("WHAAAAT????")

if number > 1000:
    print("!!!!WOOOOWWWW!!!")

# Операторы сравнения и приоритеты операций
# "<"      - меньше
# ">"      - больше
# "=="     - равно
# ">="     - больше или равно
# "<="     - меньше или равно
# "!="     - не равно
# "not"    - не является чем-то
# "is"     - является тем же самым
# "is not" - не является тем-же самым
# "in"     - является частью чего-то
# "not in" - не является частью чего-то

x = 5
y = 10
z = 15

print((x < y) and (y <= z))
print(x < y <= z)

# ---------------------
# Оператор is проверяет, являются ли оба операнда одним и тем же объектом в памяти, тогда как простое сравнение на
# равенство == проверяет только на соответствие содержимого двух операндов, но не проверяет,
# являются ли они одним и тем же объектом.
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)
print(l1 is not l2)

# Оператор in проверяет, включает ли операнд справа тот операнд, что слева:

print(3 in l1)
print(4 in l1)
print(5 not in l1)

# Альтернативный синтаксис if, замена тернарному оператору
test = True
result = 'Test is True' if test else 'Test is False'
# result = 'Test is True'

test = True
print('ttt' if test else 'fff')  # выведет ttt

# Особенности сравнения объектов
s = ''

if s != '':
    pass

if 8 % 2 != 0:
    pass

if s:
    pass

if 8 % 2:
    pass

# Еще одна альтернатива тернарному оператору

a = 11
if 10 < a < 20:
    pass


test = True
true1 = True
true2 = False
true3 = True
result = test and 'Test is True' or 'Test is False'

# В нашем случае test = True, т.е. and его пропускает и возвращает нам последнее из истинных значений,
# с которым работал, т.е. выражение 'Test is True' or 'Test is False'. Or возвращает первое встреченное true выражение,
# ему больше ничего не интересно. Если заменить строки приблизительным смыслом и использовать псевдокод,
# получим что-то вида:

result1 = true1 and true2 or true3
print("result1 =>", result1)
result2 = true2 or true3
print("result2 =>", result2)
result3 = true2
print("result2 =>", result2)

