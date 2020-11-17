class MyClass:
    def __init__(self):
        self.x=100
    def print_x(self,y=None):
        self.y=y
        if not y:
            print(self.x)
        else:
            print(self.y)




c=MyClass()

c.print_x(2)
c.print_x()
#c.print_x
print("c.x = ", c.x)
print("getattr = ", getattr(c, "x"))
print("getattr = ", getattr(c, "print_x")())
print(c.x)
print("delattr = ", delattr(c, "x"))
#print(c.x)
c.print_x(2)
c.print_x()