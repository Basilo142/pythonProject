import os


class CarBase:
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, body_whl, carrying):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try:
            l, w, h = (float(c) for c in body_whl.os.split('x', 2))
        except ValueError:
            l, w, h = .0, .0, .0

    def get_body_volume(self):


class SpecMachine(CarBase):
    pass
