import os

put = os.path.abspath('text.txt')
print(os.path.splitext('text.txt'))
print(type(put), put)

f = lambda x: x + 2

data = [1, 2, 3, 4]
f_data = [y for x in data if (y := f(x)) != 4]

print(f_data)

g = [y := f(3), y ** 2, y ** 3]
print(g)
print(y)
print("Все")
