def bread(func):
    def wrapper():
        print("<====>")
        func()
        print("</====>")

    return wrapper


def tuna():
    print("<<<Tuna>>>")


f = bread(tuna)
print(f())


def tomato(func):
    def wrapper():
        print("<<<Tomato>>>")
        func()

    return wrapper


@bread
@tomato
def test():
    print("<<<Tuna>>>")


test()


def log_call(func):
    def wrapper(*args):
        print(f"I'am calling {func}")
        return func(*args)

    return wrapper


@log_call
def greetings(name):
    return f"Hi, {name}"


@log_call
def good_bye():
    return 'Goodbye all!'


print(good_bye())


def before_and_after(func):
    def wrapper(*args):
        print("Before")
        result = func(*args)
        print("After")
        return result

    return wrapper


@before_and_after
def call_me():
    print('I am called')
    return 4


print(call_me())



