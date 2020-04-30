import sys

input()
a = []
for s in sys.stdin:
    a.append(int(s))

maxv = -2000000000000000
minv = a[0]
for i in range(1, len(a)):
    maxv = max(maxv, a[i] - minv)
    minv = min(minv, a[i])

print(maxv)
