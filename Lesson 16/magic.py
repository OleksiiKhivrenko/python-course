# Magic methods
# методы - которые неявно вызываются, начинаются и заканичваются на два нижних подчеркивания
# и заканчиваются

# __init__
# __add__
# __lz__

# Жизненый цикл объекта
# __new__ - конструктор вызывается в момент создания нового объекта
# применение - singleton для переопределения чего-то
# __init__ - инициализатор, вызывается сразу после создания объекта,
# объект передается как self в __init__
# __del__ - финализатор, вызывается сразу перед тем, как удалить объект
# вызов garbage collector вручную

def t(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(t(1, 2, 3, 4))


def t2(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


t2(first='hello', second='world')


class A:
    def __new__(cls, v, *args, **kwargs):
        print("I am in a __new__")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, v):
        print("I am in __init__")
        self.v = v

    def __del__(self):
        print("I am in a delete")


a = A("some value")
print(a.v)
del a


# Волшебство равенства
# __eq__
# __ne__

class Letter:
    def __init__(self, l):
        self.l = l

l1 = Letter('a')
l2 = Letter('b')
