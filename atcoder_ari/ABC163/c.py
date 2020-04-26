N = int(input())
d = list(map(int, input().split()))
p = [0] * N
for i in range(N - 1):
    p[d[i] - 1] += 1
for i in range(N):
    print(p[i])
