from functools import reduce


def toStr(i, j):
    return str(i) + ' ' + str(j)


input()

a = list(map(int, input().split()))
N = len(a) - 1

count = 0
for i in range(N):
    for j in range(i + 1, N + 1):
        n_j = N - j
        n_i = N - i
        if n_j < 0:
            break
        if a[n_i] < a[n_j]:
            count += 1
            tmp = a[n_i]
            a[n_i] = a[n_j]
            a[n_j] = tmp


print(reduce(toStr, a))
print(count)
