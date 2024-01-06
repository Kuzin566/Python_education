class O:
    pass


class T(O):
    pass


class H(O):
    pass


class C(T, H):
    pass


class B(T):
    pass


class A(C, B):
    pass


print(A.__mro__)
