N, A, B = map(int, input().split())

sum_som = 0
for i in range(1, N + 1):
    if A <= (sum(list(map(int, list(str(i)))))) <= B:
        sum_som = sum_som + i

print(sum_som)
