# Написать функцию перевода размеров женского белья из международного во все остальные. Внтри функции нужно просто
# обращаться к правильно составленному словарю.

def convert_from_intern_size(country, size):
    sizes = ["XXS", "XS", "S", "M", "L", "XL", "XXL", "XXXL"]
    countries = ["Russia", "Germany", "USA", "France", "GB"]
    init_sizes_by_countries = [42, 36, 8, 38, 24]
    size_increase = dict(zip(sizes, [i * 2 for i in range(len(sizes))]))
    lingerie_sizes = {size: dict(zip(countries, map(
        lambda size_amount: size_amount + size_increase[size],
        init_sizes_by_countries
    ))) for index, size in enumerate(sizes)}

    if size in lingerie_sizes and country in lingerie_sizes[size]:
        return lingerie_sizes[size][country]
    else:
        return None


print(convert_from_intern_size("Russia", "XS"))
