from functools import reduce


def toStr(i, j):
    return str(i) + ' ' + str(j)


input()
a = list(map(int, input().split()))

for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            break
        if a[i] < a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    print(reduce(toStr, a))
