import time
import os
from multiprocessing import Process

class Print(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


p = Print("Wikki")
p.start()
p.join()















# *****************************************************************
# f = open("r.txt")
# foo = f.readline()
#
# if os.fork() == 0:
#     foo = f.readline()
#     print("child:", foo)
# else:
#     foo = f.readline()
#     print("parent:", foo)

# ***************************************************************************************
# foo = "bar"
#
# if os.fork() == 0:
#     foo = "baz"
#     print("child:", foo)
# else:
#     print("parent:", foo)
#     os.wait()

# *****************************************************************************************
#
# pid = os.fork()
# if pid == 0:
#     while True:
#         print("child:", os.getpid())
#         time.sleep(5)
# else:
#     print("parent:", os.getpid())
#     os.wait()
#
# *****************************************************************************************
#
# while True:
#     print ("pid = ", pid,"time", time.time())
#     time.sleep(2)