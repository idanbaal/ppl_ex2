

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber


class Engineer(Employee):

    def __init__(self, first, last, staffnum,profession ):
        Employee.__init__(self,first, last,staffnum)
        self.profession = profession


    def GetEngineer(self):
        return self.Name() + ", " +  self.profession

class Cat():

    def __init__(self, name ):
        self.name = name


c = Cat("Mizi")

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")
z = Engineer("Homer", "Simpson", "1007","Software")




###Question 2###

def isClass(classInfo):
    return str(type(classInfo)) == "<type 'classobj'>" or str(type(classInfo)) == "<type 'type'>"

def isInstance(object1):
    return str(type(object1))== "<type 'instance'>"

def isInstancePPL(object1, classInfo):
    if isInstance(object1) and isClass(classInfo):
        return object1.__class__ is classInfo


def numInstancePPL(object1, classInfo):
    if isInstance(object1) and isClass(classInfo):
        if isInstancePPL(object1,classInfo):
            return 1
        else:
            return numSubclassPPL(object1.__class__,classInfo)


def isSubclassPPL(class1, classInfo):
    if isClass(class1) and isClass(classInfo):
        if class1 == classInfo:
            return True
        elif class1.__bases__ != ():
            return isSubclassPPL(class1.__bases__[0],classInfo)
        return False


def numSubclassPPL(class1, classInfo):
    if isClass(class1) and isClass(classInfo):
        if class1 == classInfo:
            return 1
        elif class1.__bases__ != ():
            return 1 + numSubclassPPL(class1.__bases__[0],classInfo)
        return 0

print type(y)



###Question 3###

def count_if(lst ,func):
    return len(filter(func ,lst))


def for_all(lst ,apply ,pred):
    return all(map(pred ,map(apply ,lst)))


def for_all_red(lst ,apply ,pred):
    return pred(reduce(apply, lst))


def there_exists(lst,n,pred):
    return sum(map(pred,lst)) >= n


