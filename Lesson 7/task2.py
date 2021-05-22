# Чулки и носки

# Носки
# Размер	S-M	L
# Великобританский размер	2-4	5-6
# Европейский размер	35-37	38-40
# Американский размер	4-6	6-8
# Длина стопы	21-23	23-25
# Подробнее: https://rozetka.com.ua/pantyhose_info/

def create_sizes_by_countries_type(countries, initial_size, international_sizes):
    country_sizes = {size: initial_size + index * 2 for index, size in enumerate(international_sizes)}
    return {country: country_sizes for country in countries}


def convert_from_intern_size(country, size):
    init_size_country_type_0 = "2-4"
    init_size_country_type_1 = "35-37"
    init_size_country_type_2 = "4-6"

    international_sizes = ["S", "M", "L"]

    sizes = {
        "GB": dict(zip(international_sizes, (init_size_country_type_0, init_size_country_type_0, "5-7"))),
        "EU": dict(zip(international_sizes, (init_size_country_type_1, init_size_country_type_1, "38-39"))),
        "USA": dict(zip(international_sizes, (init_size_country_type_2, init_size_country_type_2, "40-41"))),
    }

    if country in sizes and size in sizes[country]:
        return sizes[country][size]
    else:
        return None


print(convert_from_intern_size("GB", "S"))
