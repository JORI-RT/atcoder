n = int(input())

ary = []
[ary.append(int(input())) for i in range(int(n))]

if n == 1:
    print(ary[0])
elif n == 2:
    print(max(ary[0], ary[1]))
elif n == 3:
    print(min(max(ary[0], ary[1] + ary[2]),
              max(ary[0] + ary[1], ary[2]),
              max(ary[0] + ary[2] + ary[1])
              ))
else:
    print(min(
        max(ary[0], ary[1] + ary[2] + ary[3]),
        max(ary[1], ary[0] + ary[2] + ary[3]),
        max(ary[2], ary[1] + ary[0] + ary[3]),
        max(ary[3], ary[1] + ary[2] + ary[0]),
        max(ary[0] + ary[1], ary[2] + ary[3]),
        max(ary[0] + ary[2], ary[1] + ary[3]),
        max(ary[0] + ary[3], ary[2] + ary[1])
    ))
