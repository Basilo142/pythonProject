import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        # self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext[1]


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            pass

    @classmethod
    def instance(cls, row):
        return cls(
            row[1],
            row[2],
            row[3],
            row[5],
        )


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, body_whl, carrying):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try:
            l, w, h = (float(c) for c in body_whl.split('x', 2))
            # print("l=", l)
        except ValueError:
            l, w, h = .0, .0, .0
        self.body_length = l
        self.body_width = w
        self.body_height = h

    def get_body_volume(self):
        volum = self.body_length*self.body_width*self.body_height
        return volum

    @classmethod
    def instance(cls, row):
        return cls(
            row[1],
            row[3],
            row[4],
            row[5],
        )

class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
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
    with open(csv_name) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        create_strategy = {
            car_class.car_type: car_class for car_class in (Car, Truck, SpecMachine)
        }
        print(create_strategy)
        for row in reader:
            try:
                # определяем тип автомобиля
                car_type = row[0]
            except IndexError:
                # если не хватает колонок в csv - игнорируем строку
                continue

            try:
                # получаем класс, объект которого нужно создать
                # и добавить в итоговый список car_list
                car_class = create_strategy[car_type]
            except KeyError:
                # если car_type не извесен, просто игнорируем csv-строку
                continue

            try:
                # создаем и добавляем объект в car_list
                c_l.append(car_class.instance(row))
            except (ValueError, IndexError):
                # если данные некорректны, то игнорируем их
                pass

        return c_l