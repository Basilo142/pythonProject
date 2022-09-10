import itertools
count = itertools.count()

data = [100, 200, 300]
daily_data = list(zip(count, data))
print(daily_data)

print(next(count))
print(next(count))
print(next(count))
