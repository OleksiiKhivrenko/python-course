# Верхняя одежда, платья и брюки

# Написать функцию перевода размеров Верхняя одежда, платья и брюки из международного во все остальные. Внтри функции нужно просто
# обращаться к правильно составленному словарю.
def create_sizes_by_countries_type(countries, initial_size, international_sizes):
    country_sizes = {size: initial_size + index * 2 for index, size in enumerate(international_sizes)}
    return {country: country_sizes for country in countries}


def convert_from_intern_size(country, size):
    sizes = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    init_size_country_type_0 = 40
    init_size_country_type_1 = 34
    init_size_country_type_2 = 36
    init_size_country_type_3 = 38
    init_size_country_type_4 = 8
    init_size_country_type_5 = 6

    international_sizes = ["S", "M", None, "L", None, "XL", None, "XXL"]

    countries_type_0 = ["Russia"]
    countries_type_1 = ["Belgium", "Germany", "Netherlands", "Norway", "Finland", "Sweden"]
    countries_type_2 = ["France", "Switzerland"]
    countries_type_3 = ["Italy"]
    countries_type_4 = ["GB"]
    countries_type_5 = ["USA"]

    countries_types = ((countries_type_0, init_size_country_type_0), (countries_type_1, init_size_country_type_1),
                       (countries_type_2, init_size_country_type_2), (countries_type_3, init_size_country_type_3),
                       (countries_type_4, init_size_country_type_4), (countries_type_5, init_size_country_type_5))

    dict_countries_size = dict()

    for country_type in countries_types:
        dict_countries_size.update(create_sizes_by_countries_type(country_type[0], country_type[1],
                                                                  international_sizes))

    dict_sizes = {
        "international_sizes_by_index": dict(zip(international_sizes, sizes)),
        "countries_sizes_by_index": dict_countries_size
    }

    if country in dict_sizes["countries_sizes_by_index"] and size in dict_sizes["countries_sizes_by_index"][country]:
        return dict_sizes["countries_sizes_by_index"][country][size]
    else:
        return None


print(convert_from_intern_size("France", "XXL"))
