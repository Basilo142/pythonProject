from dataclasses import dataclass


@dataclass
class Calculator:
    num_1: int
    num_2: int = 0

    def sum(self, num1=None, num2=None):
        num_1 = num1 if num1 else self.num_1
        num_2 = num2 if num2 else self.num_2
        return num_1 + num_2

    def difference(self):
        return self.num_1 - self.num_2

    def multiplication(self):
        return self.num_1 * self.num_2

    def division(self):
        try:
            return self.num_1 / self.num_2
        except ZeroDivisionError:
            return 'ZeroDivisionError'

    def to_hex(self, num1=None):
        num_1 = num1 if num1 else self.num_1
        return '{0:x}'.format(num_1)


celc = Calculator(15, 3)
print(celc.sum())
print(celc.sum(23, 23))
print(celc.sum())

print(celc.difference())
print(celc.multiplication())
print(celc.division())

cal2 = Calculator(255)
print(cal2.to_hex(5))
print(cal2.to_hex())





