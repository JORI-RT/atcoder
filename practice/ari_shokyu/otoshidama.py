N, Y = map(int, input().split())


def isTrue(x, y, z, Y):
    if Y == 10000 * x + 5000 * y + 1000 * z:
        return True
    return False


for i in range(N + 1):
    for j in range(N - i + 1):
        if isTrue(i, j, N - i - j, Y):
            print(i, j, N - i - j)
            exit()

print(-1, -1, -1)
