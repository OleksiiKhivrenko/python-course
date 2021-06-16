import time


def log_me(func):
    def wrapper(self):
        print('logged')
        return func(self)

    return wrapper


def fibonacci(num):
    fib_list = []

    for i in range(0, num):
        if i == 0:
            fib_list.append(0)
        elif i == 1:
            fib_list.append(1)
        else:
            fib_list.append(sum(fib_list[-2:]))

    return fib_list


class A:
    def __init__(self, name, surname, fib_num):
        self.name = name
        self.surname = surname
        self.fib_num = fib_num

    @log_me
    def foo(self):
        print(f"My name is {self.name}")

    @staticmethod
    def bar():
        print("staticmethod")

    @classmethod
    def buz(cls):
        print(f"This is {cls.__name__}")

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    @fibonacci
    def calc_fibonacci(self):
        print(sum(fibonacci(self.fib_num)))


a = A('John', 'Doe')
a.foo()
a.buz()
print(a.full_name)
print(a.calc_fibonacci(3))
