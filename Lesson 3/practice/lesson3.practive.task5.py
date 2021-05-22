# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры
import copy

MIN_VALUE_OF_SMALL_BILL = 100


def get_small_bills(total_amount, money_dict, small_bills):
    available_bills_list = sorted(money_dict)
    available_small_bills = small_bills if len(small_bills) > 0 else list(filter(lambda a: a <= MIN_VALUE_OF_SMALL_BILL, available_bills_list))
    count = 0

    for el in available_small_bills:
        q = MAX_AVAILABLE_COUNT if money_dict[el]["quantity"] > MAX_AVAILABLE_COUNT else money_dict[el]["quantity"]
        count += money_dict[el]["value"] * q

    if count < total_amount:
        available_small_bills.append(available_bills_list[len(available_small_bills)])
        return get_small_bills(total_amount, money_dict, available_small_bills)
    else:
        return sorted(available_small_bills, reverse=True)


money = {
    20: {
        "quantity": 50,
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
        "quantity": 10,
        "value": 100
    },
    500: {
        "quantity": 5,
        "value": 500
    },
}

bank_total = 0
lowest_multiplicity = 0
MAX_AVAILABLE_COUNT = 10

for index, item in enumerate(money):
    value = money[item]["value"]
    quantity = MAX_AVAILABLE_COUNT if money[item]["quantity"] > MAX_AVAILABLE_COUNT else money[item]["quantity"]
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
    values_list = get_small_bills(amount, money, [])

    for index, item in enumerate(values_list):
        value = money[item]["value"]
        quantity = money[item]["quantity"]
        floorDivision = remainder // value

        if money[item]["quantity"] > MAX_AVAILABLE_COUNT:
            if money[item]["value"] < 100 and not remainder % 100:
                quantity = remainder % 100 // value
            else:
                quantity = MAX_AVAILABLE_COUNT

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
