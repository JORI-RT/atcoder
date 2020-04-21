# https://atcoder.jp/contests/arc004/tasks/arc004_1
import math
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
# print(d)
t = 0
x_max = 0
y_max = 0

for i in range(N):
    for j in range(N):
        x = abs(d[i][0] - d[j][0])
        y = abs(d[i][1] - d[j][1])
        if x + y > x_max + y_max:
            x_max = x
            y_max = y

print(math.sqrt(x_max ** 2 + y_max ** 2))
