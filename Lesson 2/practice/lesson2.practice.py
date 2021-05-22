num1 = int(input('Введите любое число: '))

# task 1 - Check on positive/negative
print('- Четное число' if not num1 % 2 else 'Нечетное число')

# task 2
if num1 % 2 and (not num1 % 3 and not num1 % 5) and num1 % 10:
    print('- Нечетное число, делится на 3 и на 5 одновременно и не делится на 10')

# task 3
list_dividers = []

if num1 != 0:
    counter = 1
    while counter <= abs(num1):
        if num1 % counter == 0:
            list_dividers.append(counter)
        counter += 1
else:
    list_dividers.append(0)

print('- Делители: ' + ', '.join(map(str, list_dividers)))

# task 4
# Discharge
number_of_discharge = len(str(num1))
print(f'- Количество разрядов: {str(number_of_discharge)}')

# Dividers
DEFAULT_MULTIPLIER = 2
list_dividers = []

start_number = abs(num1)
start_multiplier = DEFAULT_MULTIPLIER
while start_number >= start_multiplier:
    if not start_number % start_multiplier:
        list_dividers.append(start_multiplier)
        start_number = start_number / start_multiplier
        start_multiplier = DEFAULT_MULTIPLIER
    else:
        start_multiplier += 1

if num1 < 0:
    list_dividers.insert(0, -1)
elif len(list_dividers) == 1 and num1 >= 0:
    list_dividers.insert(0, 1)

print('- Множители: ' + ' * '.join(map(str, list_dividers)))
