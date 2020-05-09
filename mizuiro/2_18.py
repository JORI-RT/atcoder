def binary_search(A, x):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            return True
        elif A[mid] < x:
            left = mid + 1
        elif A[mid] > x:
            right = mid - 1


input()
AA = list(map(int, input().split()))
input()
T = list(map(int, input().split()))

count = 0
for t in T:
    if binary_search(AA, t):
        count += 1

print(count)
