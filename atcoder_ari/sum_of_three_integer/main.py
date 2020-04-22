# https://atcoder.jp/contests/abc051/tasks/abc051_b
# -*- coding: utf-8 -*-
K, S = map(int, input().split())
ans = 0
for i in range(0, K+1):
    for j in range(0, K+1):
        z = S-i-j
        if 0 <= z <= K:
            ans += 1
print(ans)
