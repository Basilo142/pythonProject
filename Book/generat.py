def even_range(start, end):
    current=start
    while current<end:
        yield current
        print('после yield - {}'.format(current))
        current +=2
for number in even_range(0,20):
    print(number)