# lower
print('STRING'.lower())  # => 'string'

# upper
print('string'.lower())  # => 'STRING'

# count - searching text by index
print('this is long string'.count('iss', 6, 10))
# => 1) slicing string 'is long string'
# => 2) returning first matched index

# found, rfound -
print('hello world'.find('ellk'))  # searching for left to right
print('hello world'.rfind('ello', 1, 10))  # => searching for right to left
# returning -1 if nothing found


