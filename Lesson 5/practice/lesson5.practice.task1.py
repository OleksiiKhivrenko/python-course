# Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!

def str_to_lowercase(val):
    return val.lower()


def str_to_uppercase(val):
    return val.upper()


my_list = ["TEXT 1", "TEXT 2", "TEXT 3"]
print(list(map(str_to_lowercase, my_list)))

my_list2 = ["text 1", "text 2", "text 3"]
print(list(map(str_to_uppercase, my_list2)))
