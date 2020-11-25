class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150


class Robot:

    def __init__(self, power):
        self._power = power
    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power= value
    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print('make robot useless')
        del self._power

wale_e = Robot(100)
print(wale_e.power)
wale_e.power = 200
print(wale_e.power)
wale_e.power = -100
print(wale_e.power)
print(wale_e.power)


class Robot:

    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        #sdfsdfdsfsfsd
        return self._power
wale_e= Robot(200)
print(wale_e.power)