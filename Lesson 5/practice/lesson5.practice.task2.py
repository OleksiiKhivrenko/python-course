# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map

def num_to_sqr(num):
    return num ** 2


list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num_to_sqr(4))
print(list(map(num_to_sqr, list_numbers)))
