N = int(input())
d = list(map(int, input().split()))
for j in range(1, N+1):
    count = 0
    for i in range(len(d)):
        if j == d[i]:
            count += 1
    print(count)
