# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_1_A
import sys
from functools import reduce


def to_str(i, j):
    return str(i) + ' ' + str(j)


input()
a = list(map(int, input().split()))

count = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            count += 1
    print(reduce(to_str, a))
print(count)
