from math import factorial

input()
A = list(map(int, input().split()))

s = []
for i in range(len(A)):
    s.append(i + 1 + A[i])

count = 0
AA = set(s)
for S in AA:
    s_count = s.count(S)
    if s_count == 1:
        continue
    count += factorial(s_count)// factorial(2) // factorial(s_count -2)

print(count)
