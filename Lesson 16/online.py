class D:
    pass


class F:
    pass


class E:
    pass


class B(D, E):
    pass


class C(E, F):
    pass


class A(B, C):
    pass


print(A.mro())
