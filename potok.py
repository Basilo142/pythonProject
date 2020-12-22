from threading import Thread

from threading import Thread
import time

def count(n):
    while n > 0:
        n -= 1

# series run
t0 = time.time()
count(100_000_0000)
count(100_000_0000)
print(time.time() - t0)

# parallel run
t0 = time.time()
th1 = Thread(target=count, args=(100_000_0000,))
th2 = Thread(target=count, args=(100_000_0000,))

th1.start(); th2.start()
th1.join(); th2.join()
print(time.time() - t0)







# from concurrent.futures import ThreadPoolExecutor, as_completed
#
# def f(a):
#     return a * a
#
#
# with ThreadPoolExecutor(max_workers=3) as pool:
#     results = [pool.submit(f, i) for i in range(10)]
#
#     for future in as_completed(results):
#         print(future.result())
#
#
#
#
#
#











# from concurrent.futures import ThreadPoolExecutor, as_completed
#
# def f(a):
#     return a * a
#
#
# with ThreadPoolExecutor(max_workers=3) as pool:
#     results = [pool.submit(f, i) for i in range(10)]
#
#     for future in as_completed(results):
#         print(future.result())
#
#
#
#
#
#







# **************************************
# class Pr(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print("Hello", self.name)
#
#
# th = Pr("MIKI")
# th.start()
# th.join()
#**************************************
# def f(name):
#     print('Hello', name)
#
#
# th = Thread(target=f, args=('Bibi',))
# th.start()
# th.join()
