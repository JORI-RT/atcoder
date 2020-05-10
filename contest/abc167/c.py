import itertools
import sys
import numpy as np

N, M, X = map(int, input().split())
C = []
for n in range(N):
    C.append(list(map(int, input().split())))

result = []
for n in range(2 ** N):
    ii = [0] * N
    for i in range(N):
        if (n >> i) & 1:
            ii[i] = 1
    # print(ii)
    tmp = [0] * (M + 1)
    for j in range(len(ii)):
        if ii[j] == 1:
            tmp = (np.array(tmp) + np.array(C[j])).tolist()
    result.append(tmp)


def ex(array):
    for i in array[1:]:
        if i < X:
            return False
    return True


min_value = sys.maxsize
result.sort()
for r in result:
    if ex(r):
        print(r[0])
        exit()

print(-1)
