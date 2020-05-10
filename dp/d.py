N, W = map(int, input().split())

DP = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
# DP[2][3] ... i番目までをナップサックに入れることが可能なとき（成約３）
for n in range(N):
    w_i, v_i = map(int, input().split())
    for w in range(W+1):
        tmp = 0
        if w - w_i >= 0:  # i番目のやつが入れる余地があるときここがkey
            DP[n + 1][w] = max(DP[n][w - w_i] + v_i, DP[n][w])
        else:
            DP[n + 1][w] = DP[n][w]

print(max(DP[N]))