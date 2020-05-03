N, M = map(int, input().split())
H = list(map(int, input().split()))

a = []
for i in range(M):
    A, B = map(int, input().split())
    a.append([A, B])

count = 0

for i in range(1, N + 1):
    h_i = H[i - 1]
    a_i = []
    for j in a:
        if j[0] == i:
            a_i.append(j[1])
        elif j[1] == i:
            a_i.append(j[0])
    flg = True
    for k in a_i:
        if h_i <= H[k - 1]:
            flg = False
    if flg:
        count = count + 1

print(count)
