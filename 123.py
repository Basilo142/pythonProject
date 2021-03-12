try:
    x=1/0
except ZeroDivisionError:
    try:
        x=1/0
        print('w1')
    except ZeroDivisionError:
        print('w2')
