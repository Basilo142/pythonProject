import os
import csv


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        # self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            pass

    @classmethod
    def instance(cls, row):
        return cls(
            row[1],
            row[3],
            row[5],
            row[2],
        )


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

        try:
            l, w, h = (float(c) for c in body_whl.split('x', 2))
        except ValueError:
            l, w, h = .0, .0, .0

        self.body_length = l
        self.body_width = w
        self.body_height = h

    def get_body_volume(self):

        vol = self.body_length*self.body_width*self.body_height
        return vol

    @classmethod
    def instance(cls, row):
        return cls(
            row[1],
            row[3],
            row[5],
            row[4],
        )


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def instance(cls, row):
        return cls(
            row[1],
            row[3],
            row[5],
            row[6],
        )


def get_car_list(csv_name):
    c_l = []
    jp = ['.jpg', '.jpeg', '.png', '.gif']
    with open(csv_name) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        create_strategy = {
            car_class.car_type: car_class for car_class in (Car, SpecMachine, Truck)
        }

        for row in reader:
            try:
                j12 = os.path.splitext(row[3])
                j2 = j12[1]
                j1 = jp.index(j2)
                e = 1 / (len(row[0]) * len(row[1]) * len(row[3]) * len(row[5]))
            except (IndexError, ValueError, ZeroDivisionError):
                continue

            try:
                car_type = row[0]
            except IndexError:
                continue

            try:
                car_class = create_strategy[car_type]
            except KeyError:
                continue

            if row[0] == 'car' and row[2] == '':
                continue
            if row[0] == 'spec_machine' and row[6] == '':
                continue

            try:
                c_l.append(car_class.instance(row))
            except (ValueError, IndexError):
                continue

        return c_l
