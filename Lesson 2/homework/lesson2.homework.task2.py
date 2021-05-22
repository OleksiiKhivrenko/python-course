# Data TYPES

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

# Boolean algebra (logical operators)
# if

# Assignment expresion
some_list = [1, 2, 3]
if (list_length := len(some_list)) > 2:
    print("List length of", list_length, "is too long")


# Lambda expression
def func(n):
    return lambda a, b, c: (a + b + c) * n


double = func(2)
test_on_double = 'Doubled' if double(2, 3, 4) == 18 else 'Not doubled'
print(test_on_double)

# Boolean OR
num1 = 10
num2 = 20

if 0 or num1 or num2:
    print('Getting first true from condition num1 (false or true or true) =>', 0 or num1 or num2)

if 0:
    print("Won't see this print")

# Boolean AND
num1 = 10
num2 = 20

if 0 and num1 and num2:
    print('\nNot getting anything (false and true and true), condition equal to false =>', 0 and num1 and num2)

if num1 and 0 and num2:
    print('Not getting anything (false and true and true), condition equal to false =>', 0 and num1 and num2)

if num1 and (0 or num2):
    print('Getting num2 since we\'re looking for false in expression =>', num1 and (0 or num2))

# Boolean NOT

if (not 0) == (not False):
    print('\nprint is visible since not 0 equal to not False => True')

# Comparisons
# in
test_list = [1, 2, 'str', False]
test_tuple = (2, True, 0)
test_dict = {'a': 1, 'str': 'string'}

if False in test_list:
    print('\nprint is visible since False inside test_list')

if 2 in test_list:
    print('print is visible since 2 inside test_list')

if True in test_tuple:
    print('print is visible since True inside test_tuple')

if 'a' in test_dict:
    print("matching the prop inside dict")

# in, not in

if False in test_list:
    print('\nprint is visible since False inside test_list')

if 2 in test_list:
    print('print is visible since 2 inside test_list')

if True in test_tuple:
    print('print is visible since True inside test_tuple')

if 'a' in test_dict:
    print("matching the prop inside dict")

if 'a' not in test_dict:
    print("matching the prop inside dict")
else:
    print('"a" prop in the dict')

# is, is not, ==, !=
num3 = 2
num4 = num3
num5 = 2
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

# is, is not
if num3 is num4:
    print("\nnum3 and num4 are using the same link")

if num5 is num3:
    print("num5 is num3 since all simple types are using the same link")

if list2 is not list3:
    print("list and list3 are not using the same link")

dict1 = {'a': 1}
dict2 = dict1
dict3 = {'a': 1}

if dict1 is dict3:
    print('2 dicts with the same props are using the same link')

# ==, !=
if num3 == num4:
    print("\nthe same value")

if num3 != num4:
    pass
else:
    print("\nnot the same value")

# <, <=, >, >=
num1 = 5
num2 = 10

if num2 > num1:
    print("num2 is more then num1")

if num1 < num2:
    print("num1 is less then num2")

if num2 >= num2:
    print("true, since num2 == num2")

if num1 >= num1:
    print("true, since num1 == num1")




