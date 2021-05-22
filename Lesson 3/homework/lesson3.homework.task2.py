# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись

# далее открываем файл на чтение (опция 'r')
f = open("task2.txt", 'r')  # в файле теперь file descriptor


def calculate_fizzbuzz(fizz, buzz, num3):
    j = 1
    list_of_strings = []

    while j <= num3:
        if not j % fizz and not j % buzz:
            list_of_strings.append('FB')
        elif not j % fizz:
            list_of_strings.append('F')
        elif not j % buzz:
            list_of_strings.append('B')
        else:
            list_of_strings.append(j)
        j += 1

    return " ".join(map(str, list_of_strings))


# Проверка всех строк вместо 30 (для 30 можно использовать while)
for line in f:
    str_list_first_line = line.split(" ")

    if len(str_list_first_line) < 3:
        print("The amount of numbers less than 3")
        continue

    num_list = [int(i) for i in str_list_first_line]

    result = calculate_fizzbuzz(num_list[0], num_list[1], num_list[2])
    print(result)

f.close()  # закрытие файла
