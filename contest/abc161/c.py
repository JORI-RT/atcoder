N, K = map(int, input().split())

cm = N
k = N % K
if k == 0:
    print(0)
    exit()
print(min(abs(k-K), N))
