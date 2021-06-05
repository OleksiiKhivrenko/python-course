# mro - порядок в котором будут искаться реализации метода
# message resolution order - порядок определения методов

class Base:
    def __init__(self):
        print(f"I am in Base")


class A(Base):
    def __init__(self):
        print(f"I am in A")
        super().__init__()


class B(Base):
    def __init__(self):
        print(f"I am in B")
        super().__init__()


class C(A, B):
    def __init__(self):
        print(f"I am in C")
        super().__init__()


c = C()
