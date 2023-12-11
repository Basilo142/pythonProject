class Car:
    def __init__(self):
        self._type = None

    def get_type(self):
        return self._type

    def __repr__(self):
        return self._type


class WorkerCar(Car):
    def __init__(self):
        super().__init__()
        self._type = 'Car for work'


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self._type = 'Sport Car'


class CarFactory:
    def __init__(self):
        self._cars = {}

    def register(self, car_type, car_class):
        self._cars[car_type] = car_class

    def create_car(self, car_type):
        if car_type not in self._cars:
            raise ValueError('Invalid Car')
        return self._cars[car_type]()


if __name__ == '__main__':
    factory = CarFactory()
    factory.register('ww', SportCar)
    c = factory.create_car('ww')
    print(c)
    d = factory.create_car('rr')
