from contracts import contract


# @contract(x='int,>=0')
def f(x):
    x = int(input("Enter positive number, please: "))
    assert x > 0, "Value should be positive!"

f(-5)
print(f(10))
