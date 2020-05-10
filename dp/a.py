N = int(input())
H = list(map(int, input().split()))
DP = [0] * N  # N番目までに使用する最小エネルギ-
for n in range(1, N):
    if n == 1:
        DP[1] = abs(H[1] - H[0])
    else:
        DP[n] = min(abs(H[n] - H[n - 2]) + DP[n - 2], abs(H[n] - H[n - 1]) + DP[n - 1])
print(DP[-1])
