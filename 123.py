import os
import csv

def get_car_list(csv_name):
    c_l = []
    with open(csv_name) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            print(row)



s = get_car_list('cars.csv')














# put = os.path.abspath('text.txt')
# print(os.path.splitext('text.txt'))
# print(type(put), put)
#
# f = lambda x: x + 2
#
# data = [1, 2, 3, 4]
# f_data = [y for x in data if (y := f(x)) != 4]
#
# print(f_data)
#
# g = [y := f(3), y ** 2, y ** 3]
# print(g)
# print(y)
# print("Все")
