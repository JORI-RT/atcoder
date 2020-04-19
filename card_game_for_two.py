# https://atcoder.jp/contests/abc088/tasks/abc088_b

input()

AT = 0
Nob = 0
count = 0
for i in reversed(sorted(list(map(int, input().split())))):
    if(count % 2 == 0):
        AT += i
    else:
        Nob += i
    count += 1
print(AT-Nob)
