N, K = map(int, input().split())

max_n = 0
result = set()
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in A:
        result.add(j)

print(N - len(result))
