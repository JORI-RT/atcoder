N, M, Q = map(int, input().split())

s = 0
As = []

for j in range(N):
    for i in range(1, M):
        A = []
    A.append(i)

print(As)

A = [1, 3, 4]

for i in range(Q):
    a, b, c, d = map(int, input().split())
    if A[b - 1] - A[a - 1] == c:
        s += d

print(s)
