# task1 сумма списка при помощи for и while

my_list = [10, 20, 30, 40]
i = 0
total = 0

while i < len(my_list):
    total += my_list[i]
    i += 1

print(f"sum of {my_list} with while: {total}")

my_list2 = [20, 30, 40]
total2 = 0
for index, item in enumerate(my_list2):
    total2 += item

print(f"sum of {my_list2} with for: {total2}")

total3 = 0
for item in list(range(10, 20, 5)):
    total3 += item

print(f"sum of {range(10, 30, 5)} with for: {total3}")
