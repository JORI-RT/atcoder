import math
from functools import reduce


def gcd(*numbers):
    return reduce(my_gcd, numbers)


def my_gcd(i, j):
    if i > j:
        a = i
        b = j
    elif i == j:
        return i
    else:
        a = j
        b = i
    r = a % b

    if r == 0:
        return b
    return my_gcd(b, r)


K = int(input()) + 1
sum = 0
for i in range(1, K):
    for j in range(1, K):
        for k in range(1, K):
            sum += gcd(i, j, k)

print(sum)
