# Третий уровень ("Мистер Буль. Джордж Буль!"):
# Задача fizz-buzz:

# У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz.
# До третьего необходимо досчитать от единицы. Считая, надо выводить число.
# Если число кратно fizz - надо выводить F вместо числа. Если число кратно buzz - надо выводить B вместо числа.
# Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.
#
# Пример условия и результата:
# Введены числа 2, 5, 18
# Вывод должен быть таким:
# 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

fizz = int(input("Fizz: "))
buzz = int(input("Buzz: "))
number3 = int(input("Input number 3: "))

i = 1
list_of_strings = []

while i <= number3:
    if not i % fizz and not i % buzz:
        list_of_strings.append('FB')
    elif not i % fizz:
        list_of_strings.append('F')
    elif not i % buzz:
        list_of_strings.append('B')
    else:
        list_of_strings.append(i)
    i += 1

print(" ".join(map(str, list_of_strings)))


