import sys

N, K = map(int, input().split())
H = list(map(int, input().split()))
DP = [0] * N  # N番目までに使用する最小エネルギ-
for n in range(1, N):
    if n == 1:
        DP[1] = abs(H[1] - H[0])
    else:
        min_value = sys.maxsize
        for j in range(1, K + 1 if K < n else n+1):
            tmp_dpn = abs(H[n] - H[n - j]) + DP[n - j]
            if tmp_dpn < min_value:
                min_value = tmp_dpn
        DP[n] = min_value
print(DP[-1])
