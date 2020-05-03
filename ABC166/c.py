N, M = map(int, input().split())
H = list(map(int, input().split()))

r = [1] * len(H)
a = []
for i in range(M):
    A, B = map(int, input().split())
    if H[A - 1] >= H[B - 1]:
        r[B - 1] = 0
    if H[B - 1] >= H[A - 1]:
        r[A - 1] = 0

print(r.count(1))
