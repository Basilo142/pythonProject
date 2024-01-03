from typing import List
from typing import Union

Data = List[float | int]


def my_mul(data: Data) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


print(my_mul([1, 2, 3]))

Number = Union[float, int]


def add(x: Number, y: Number) -> Number:
    return x + y


print(add(3, 2.2))

from typing import TypeVar

T = TypeVar("T", int, str, float)


def calculator(x: T, y: T) -> T:
    return x + y


print(calculator(3, 77))
print(calculator("Hello", "World"))
print(calculator(3.5, 1))

