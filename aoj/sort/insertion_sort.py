# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_1_A
import sys
from functools import reduce


def to_str(x, y):
    return str(x) + ' ' + str(y)


input()
A = list(map(int, input().split()))

print(reduce(to_str, A))
for i in range(1, len(A)):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = v
    print(reduce(to_str, A))

# A[i}がどこに入ればよいかという観点
