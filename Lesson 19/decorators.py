def my_decorator(func):
    def log_call():
        print(f"I'll call {func} now")
        r = func()
        print(f"I'll called {func}")
        return r

    return log_call


def hi():
    print('hello')


hi = my_decorator(hi)
hi()


@my_decorator
def bye():
    print('bye')


bye()
