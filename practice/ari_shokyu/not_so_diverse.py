N, K = map(int, input().split())
A = list(map(int, input().split()))
a = {}
for i in range(len(A)):
    a[A[i]] += 1
