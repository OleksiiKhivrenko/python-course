import sys

filename = sys.argv[0]
print(sys.argv)
# далее открываем файл на чтение (опция 'r')
f = open(filename, 'r')  # в файле теперь file descriptor
for line in f:  # для каждой строки в файле
    print(line)
f.close()  # закрытие файла
