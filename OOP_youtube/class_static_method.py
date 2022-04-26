class Vector:
    MIN_VAL = 0
    MAX_VAL = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_VAL <= arg <= cls.MAX_VAL

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.num(self.x, self.y))

    def get_coor(self):
        print(self.x, self.y)

    @staticmethod
    def num(x, y):
        return x * x + y * y


v = Vector(1, 8)
v.get_coor()
w = Vector(100, 400)
w.get_coor()