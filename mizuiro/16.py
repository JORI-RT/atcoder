import itertools
import math

N = int(input())
P = tuple(list(map(int, input().split())))
Q = tuple(list(map(int, input().split())))

a = 0
b = 0
count = 0
for i in itertools.permutations([i for i in range(1, N + 1)]):
    count += 1
    if i == P:
        a = count
    if i == Q:
        b = count

print(abs(a - b))
