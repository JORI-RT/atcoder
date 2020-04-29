import math
from functools import reduce


def sumsum(*num):
    return reduce(su, num)


def su(a, b):
    return a + b


print(sumsum(1, 2, 3, 4))
