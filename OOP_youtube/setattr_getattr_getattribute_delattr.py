class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        print('__getattribute__{}'.format(item))
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('__setattr__, key-{}, value-{}'.format(key, value))
        if key == 'z':
            raise AttributeError('Attribute Error!!!!')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('__getattr__: {}'.format(item))

    def __delattr__(self, item):
        print('__delattr__: {}'.format(item))
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt2.x)
pt1.w = 44
pt1.z
del pt1.w

