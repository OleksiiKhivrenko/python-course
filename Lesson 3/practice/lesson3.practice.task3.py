import sys

filename = sys.argv[0]
print(sys.argv)
# далее открываем файл на чтение (опция 'r')
f = open(filename, 'r')  # в файле теперь file descriptor
my_list = []
for line in f:  # для каждой строки в файле
    my_list.append(line)
my_list.reverse()
print("".join(my_list))
f.close()  # закрытие файла
