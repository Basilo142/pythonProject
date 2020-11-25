class My:
    @staticmethod
    def f1(x,y):
        return x+y
    def f2(self, x, y):
        return x+y
    def f3(self, x, y):
        return My.f1(x, y)

print(My.f1(10,20))
c=My()
print(c.f1(30, 30))
print(c.f2(40, 40))
print(c.f3(50, 50))
print(My.f1(33,33))

class My:
    @classmethod
    def f1(cls,x):
        print(cls, x)
My.f1(3)
#print(My.f1(33,33))

class Proper:
    def __init__(self, num):
        self.num = num
    def get (self):
        return self.num
    def set(self, num):
        self.num = num
    def dell(self):
        del self.num
    v=property(get, set, dell, 'Cтрока документации')

c=Proper(5)
print("c.v", c.v)
c.v = 22
print(c.v)
del c.v
#print(c.v)
