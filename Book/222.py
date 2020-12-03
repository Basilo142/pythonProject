import random
import datetime
a = str(random.randint(0,1000))
print(type(a))
a = random.randint(0,1000)
print(type(a))
b=datetime.datetime.today().strftime("%Y%m%d%H%M%S")
print(b)
print(type(b))