import math

A, B, N = map(int, input().split())

max_v = 0
for i in range(1, N + 1):
    current_max_v = math.floor(A * i // B) - A * math.floor(i / B)
    max_v = max(max_v, current_max_v)
    # 循環したらとめる
    if i > 100000000000:
        break
print(max_v)
