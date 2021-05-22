# Банкомат выдает сумму максимально возможными купюрами
import copy

money = {
    20: {
        "quantity": 5,
        "value": 20
    },
    200: {
        "quantity": 10,
        "value": 200
    },
    10: {
        "quantity": 40,
        "value": 10
    },
    100: {
        "quantity": 1,
        "value": 100
    },
}

values_list = sorted(money, reverse=True)

bank_total = 0
lowest_multiplicity = 0

for index, item in enumerate(money):
    value = money[item]["value"]
    quantity = money[item]["quantity"]
    total_by_value = value * quantity
    bank_total += total_by_value

    if lowest_multiplicity == 0 or lowest_multiplicity > value and total_by_value >= 100:
        lowest_multiplicity = value

amount = int(input(f"Введите сумму, кратную {lowest_multiplicity}: "))
result = ''
counted_total = 0
remainder = copy.deepcopy(amount)

if amount % lowest_multiplicity:
    print(f'Введена ссума не кратная {lowest_multiplicity}')
elif amount > bank_total:
    print("Недостаточно денег")
else:
    for index, item in enumerate(values_list):
        value = money[item]["value"]
        quantity = money[item]["quantity"]
        floorDivision = remainder // value

        if counted_total < amount and value <= remainder and floorDivision > 0:
            available_quantity = 0

            if quantity < floorDivision:
                available_quantity = quantity
            elif floorDivision <= quantity:
                available_quantity = floorDivision

            counted_total += available_quantity * value
            remainder = amount - counted_total
            result += f"UAH: {value}, Q: {available_quantity}, {value}*{available_quantity}={value * available_quantity}\n"

    print(result)
    print("Total amount: ", counted_total)
