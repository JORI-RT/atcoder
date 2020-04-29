N = int(input())
S = input()

count = 0


def rgb(i, j):
    if i == 'R' and j == 'G':
        return 'B'
    if i == 'R' and j == 'B':
        return 'G'
    if i == 'G' and j == 'R':
        return 'B'
    if i == 'G' and j == 'B':
        return 'R'
    if i == 'B' and j == 'R':
        return 'G'
    if i == 'B' and j == 'G':
        return 'R'


for i in range(N -2):
    rgb_i = S[i]
    for j in range(i, N -1):
        rgb_j = S[j]
        if rgb_i == rgb_j:
            continue
        rgb_k = rgb(rgb_i, rgb_j)
        count += S.count(rgb_k, j + 1)
        if j + j -i < N and S[j + (j-i)] == rgb_k:
            count = count -1

print(count)
