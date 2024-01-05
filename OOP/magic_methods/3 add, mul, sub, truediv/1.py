"""
__sub__(self, other)	отвечает за операцию вычитания с помощью оператора -
__mul__(self, other)	отвечает за операцию умножения с помощью оператора *
__truediv__(self, other)	отвечает за операцию обычного деления с помощью оператора /
__floordiv__(self, other)	отвечает за операцию целочисленного деления с помощью оператора //
__mod__(self, other)	отвечает за операцию остатка от деления при помощи оператора %
__divmod__(self, other)	деление с остатком, определяет поведение для встроенной функции divmod(...)
__pow__(self, other[, modulo])	отвечает за операцию возведение в степень с помощью оператора **
__lshift__(self, other)	отвечает за операцию двоичного сдвига влево с помощью оператора <<
__rshift__(self, other)	отвечает за операцию двоичного сдвига вправо с помощью оператора >>
__and__(self, other)	отвечает за двоичную операцию «И» с помощью оператора &
__xor__(self, other)	отвечает за двоичную операцию «исключающее ИЛИ» при помощи оператора ^
__or__(self, other)	отвечает за двоичную операцию «ИЛИ »с помощью оператора |
__radd__(self, other)
__rsub__(self, other)
__rmul__(self, other)
__rtruediv__(self, other)
__rfloordiv__(self, other)
__rmod__(self, other)
__rdivmod__(self, other)
__rpow__(self, other[, modulo])
__rlshift__(self, other)
__rrshift__(self, other)
__rand__(self, other)
__rxor__(self, other)
__ror__(self, other)"""


class Banc_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Клиент {self.name} с балансом {self.balance}"

    def __add__(self, other):
        if isinstance(other, Banc_account):
            other = other.balance
        if not isinstance(other, (int, float)):
            raise NotImplemented('Хуйня какая то передана, необходимо int либо float')
        return Banc_account(self.name, self.balance + other)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Banc_account):
            other = other.balance
        if not isinstance(other, (int, float)):
            raise NotImplemented('Хуйня какая то передана, необходимо int либо float')
        return self.balance * other

    def __rmul__(self, other):
        return self * other


b = Banc_account('Ivan', 900)
c = Banc_account('Коля', 2)
n = b + c
print(n)
print(b * c)
# print(b + 300)
# print(2 * b)
