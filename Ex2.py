from math import sqrt

###Question 1###


class ComplexNum:
    def __init__(self, a, b=0.0):
        self.a = float(a)
        self.b = float(b)

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
        if self.re() == 0:
            return "%gi" % self.im()
        else:
            return "%g %s %gi" % (self.re(), sign, abs(self.im()))


###Question 2###

def isClass(classInfo):
    return str(type(classInfo)) == "<type 'classobj'>" or str(type(classInfo)) == "<type 'type'>"


def isInstance(object1):
    return str(type(object1)) == "<type 'instance'>"


def isInstancePPL(object1, classInfo):
    if isInstance(object1) and isClass(classInfo):
        return object1.__class__ is classInfo
    return False


def numInstancePPL(object1, classInfo):
    if isInstance(object1) and isClass(classInfo):
        if isInstancePPL(object1, classInfo):
            return 1
        else:
            return numSubclassPPL(object1.__class__, classInfo)
    return 0


def isSubclassPPL(class1, classInfo):
    if isClass(class1) and isClass(classInfo):
        if class1 == classInfo:
            return True
        elif class1.__bases__ != ():
            return isSubclassPPL(class1.__bases__[0], classInfo)
    return False


def numSubclassPPL(class1, classInfo):
    if isClass(class1) and isClass(classInfo):
        if class1 == classInfo:
            return 1
        elif class1.__bases__ != () and isSubclassPPL(class1, classInfo):
            return 1 + numSubclassPPL(class1.__bases__[0], classInfo)
    return 0



###Question 3###

def count_if(lst, func):
    if type(lst) == list and callable(func):
        try:
            return len(filter(func, lst))
        except:
            return 0
    return 0


def for_all(lst, apply, pred):
    if type(lst) == list and callable(apply) and callable(pred):
        try:
            return all(map(pred, map(apply, lst)))
        except:
            return False
    return False


def for_all_red(lst, apply, pred):
    if type(lst) == list and callable(apply) and callable(pred):
        try:
            return pred(reduce(apply, lst))
        except:
            return False
    return False


def there_exists(lst, n, pred):
    if type(lst) and type(n) == int and callable(pred):
        try:
            return sum(map(pred, lst)) >= n
        except:
            return False
    return False



