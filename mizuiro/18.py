n = int(input())
A = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def bin_search(Array, x):
    left = 0
    right = len(Array)-1
    mid = (left + right) // 2
    while left <= right:
        if Array[mid] == x:
            return True
        if Array[mid] > x:
            right = mid - 1
        elif Array[mid] < x:
            left = mid + 1
        mid = (left + right) // 2
    return False


count = 0
for i in T:
    if bin_search(A, i):
        count += 1

print(count)
