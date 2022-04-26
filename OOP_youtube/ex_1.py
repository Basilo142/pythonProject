class Point:
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print('__new__ for {}'.format(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('This is __init__ for {}'.format(self))
        self.x = x
        self.y = y

    def __del__(self):
        print('Delleting !!!! ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return(self.x, self.y)


pt2 = Point(2, 66)

print(pt2.y, pt2.x)
