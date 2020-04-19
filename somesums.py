n, a, b = map(int, input().split())

i = 1
total = 0
for i in range(n+1):
    if(a <= i and b >= i):
        total += i

print(total)
