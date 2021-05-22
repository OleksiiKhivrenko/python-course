def sum_two_values(a):
    def second_value(b):
        return a + b

    return second_value


my_test = sum_two_values(5)
my_test3 = my_test(6)
print(sum_two_values(2)(3))
print(my_test3)
