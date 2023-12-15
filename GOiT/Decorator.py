import time
from functools import wraps


def wrong_loger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func}: {end-start}')
        return result
    return wrapper


@wrong_loger
def loop(num):
    while num > 0:
        num -= 1



loop(100000000)
print(loop.__name__)
