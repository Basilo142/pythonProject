class MyClass(object):
    i = 123

    def __init__(self):
        self.i = 345

print('MyClass().i = ',MyClass().i)

print("MyClass = ", MyClass.i)
