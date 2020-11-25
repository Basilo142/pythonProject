def deco(C):
    try:
        x=1/0
    except ZeroDivisionError:
        print("Деление на ноль !!!")
        x=0
    print("Внутри декора")
    print(x)
    return C





@deco
class MyClass(object):
    i = 123

    def __init__(self):
        self.i = 345

print('MyClass().i = ',MyClass().i)

print("MyClass = ", MyClass.i)

