N = int(input())

sum = 0
for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
        pass
    else:
        sum += i

print(sum)
