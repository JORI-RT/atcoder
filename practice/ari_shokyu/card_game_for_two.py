N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)

Alice_sum = 0
Bob_sum = 0
for i in range(len(sorted_A)):
    if i % 2 == 0:
        Alice_sum = Alice_sum + sorted_A[i]
    else:
        Bob_sum = Bob_sum + sorted_A[i]

print(Alice_sum - Bob_sum)
