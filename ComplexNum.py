from math import sqrt


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def re(self):
        return self.a

    def im(self):
        return self.b

    def tuple_to(self):
        return self.re(), self.im()

    def abs(self):
        return sqrt((self * self.conjugate()).re())

    def conjugate(self):
        return ComplexNum(self.re(), -self.im())

    def __mul__(self, other):
        if isinstance(self, other.__class__):
            return ComplexNum(self.re() * other.re() - self.im() * other.im(),
                              self.re() * other.im() + self.im() * other.re())
        else:
            raise TypeError("Complex multiplication only defined for Complex Numbers")

    def __neg__(self):
        return ComplexNum(-self.re(), -self.im())

    def __add__(self, other):
        if isinstance(self, other.__class__):
            return ComplexNum(self.re() + other.re(), self.im() + other.im())

    def __sub__(self, other):
        if isinstance(self, other.__class__):
            return self + -other

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.im() == other.im() and self.re() == other.re()
        else:
            return False

    def __repr__(self):
        sign = "+" if self.im() >= 0 else "-"
        return "%d %s %di" % (self.re(), sign, abs(self.im()))
