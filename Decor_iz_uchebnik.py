def dec1(f):
    print('#1')
    return f
def dec2(f):
    print('#2')
    return f
@dec1
@dec2
def func(x):
    print("func")
    return 'x= {}'.format(x)
print(func(10))

func(20)
