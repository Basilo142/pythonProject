from itertools import zip_longest


class First(object):
    def f1(self):
        print('f1 in First')

    def s1(self):
        print('s1 in First')


class Second2(First):
    def s1(self):
        print('s1 in second2')


class Second1(First):
    def s1(self):
        print('s1 in second1')


class Finely(Second2, Second1):
    def fin1(self):
        print('fin in Finely')




s = Finely()
s.fin1()
s.s1()
series = [1, [2, 3], 4, [5, [6, 7]], [[8]], 9, 10]
ex_list = []


def list_to_list(series):
    for i in series:
        if type(i) == list:
            list_to_list(i)
        else:
            ex_list.append(i)
    return ex_list


new_series = list_to_list(series)
print(new_series)

for i in series:
    pass
else:
    print(i)
print(series.index(i))


def func(series, n, filler=None):
    return zip_longest(*[iter(series)] * n, fillvalue=filler)


for i in func(new_series, 7):
    print(i)


