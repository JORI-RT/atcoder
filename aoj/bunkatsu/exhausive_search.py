n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))


def solve(i, m):
    if m == 0:
        return 1
    if i >= n:
        return 0
    res = solve(i + 1, m) or solve(i + 1, m - A[i])
    return res
