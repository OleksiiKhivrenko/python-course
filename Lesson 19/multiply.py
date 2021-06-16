def multiply(multiplier):
    def decorator(func):
        def wrapper():
            print('Before')
            result = func()
            print("After")
            result *= multiplier
            return result

        return wrapper

    return decorator


@multiply(10)
def get_4() -> int:
    print('I am called')
    return 4


@multiply(20)
def get_20() -> int:
    print('I am called')
    return 4


print(get_4(), get_20())
