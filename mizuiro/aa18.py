n = int(input())
A = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def bin_search(Array, x):
    left = 0
    right = len(Array)
    mid = (left + right) // 2
    while left > right:
        if Array[mid] == x:
            return True
        if Array[mid] >= x:
            right = right // 2
        elif Array[mid] < x:
            left = mid + 1
        mid = (left + right) // 2
    return False


print(bin_search(A, 3))
