def accumulator():
    total = 0
    while True:
        value = yield total
        print('Go: {}'.format(value))
        if not value:
            break
        total += value


generator = accumulator()
next(generator)
print("print--- {}".format(generator.send(1)))
print("print--- {}".format(generator.send(1)))
print("print--- {}".format(generator.send(1)))

w = (1, 2, 'e')
print(w)
print(type(w))
print(type(w[0]))
print(type(w[2]))
