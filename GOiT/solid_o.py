from math import pi


class Shape:
    def area_of(self):
        raise NotImplemented


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area_of(self):
        return self.side ** 2


class AreaCalculator:
    def __init__(self, shapes: list):
        self.shapes = shapes

    def total_area(self):
        sum = 0
        for el in self.shapes:
            sum += el.area_of()
        return sum


if __name__ == '__main__':
    shapes = AreaCalculator([Rect(10, 10), Square(5), Rect(4, 5), Rect(3, 3), Circle(3)])
    area = shapes.total_area()
    print(area)
