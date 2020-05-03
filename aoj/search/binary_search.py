# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_B


def bs(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return True
        elif A[mid] > key:
            right = mid
        else:
            left = mid + 1
    return False


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
C = 0
for t in T:
    if bs(S, t):
        C = C + 1

print(C)
