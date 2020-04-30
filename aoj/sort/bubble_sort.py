# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_1_A
import sys
from functools import reduce


def to_str(x, y):
    return str(x) + ' ' + str(y)


n = int(input())
A = list(map(int, input().split()))

count = 0
flag = 1
while flag:
    flag = 0
    for j in range(n):
        if j <= n - 2 and A[j] > A[j + 1]:
            tmp = A[j + 1]
            A[j + 1] = A[j]
            A[j] = tmp
            count += 1
            flag = 1

print(reduce(to_str, A))
print(count)
