# https://atcoder.jp/contests/abc088/tasks/abc088_b

input()

a = sorted(map(int, input().split()), reverse=True)
print(sum(a[::2]) - sum(a[1::2]))
