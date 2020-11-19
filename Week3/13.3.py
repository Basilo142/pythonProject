class Class1:
    def fun1(self):
        print("fun1 from Class1")

    def fun2(self):
        print("fun2 from Class1")


class Class2(Class1):
    def fun3(self):
        print("fun3 from Class2")


class Class3(Class1):
    def fun3(self):
        print("fun3 from Class3")

    def fun4(self):
        print("fun4 from class3")


class Class4(Class3, Class2):
    def fun3(self):
        print("fun3 from Class4")


print("Class1", Class1.__bases__)
print("Class2", Class2.__bases__)
print("Class3", Class3.__bases__)
print("Class4", Class4.__bases__)

c = Class4()
print("c.fun1()", end=" ")
c.fun1()
print("c.fun1()", end=" ")
c.fun2()

# b=Class2()
# b.fun3()
c.fun3()
c.fun4()

print(Class4.__mro__)


class C0:
    x = 10


class C1(C0):
    pass


class C2(C1):
    pass


class C3(C2):
    pass


class C4(C3):
    pass


class C5(C4):
    pass


class C6(C5):
    pass


class C7(C2):
    pass


class C8(C6):
    pass


class C9(C7):
    pass


class C10(C8, C9):
    pass


print("C10", C10.__mro__)


class Dsa:
    def __init__(self):
        self.i = 20

    def __getattr__(self, item):
        print("якась хуйня")
        return 0


s = Dsa()
print(s.i)
print(s.er)
