N, M = map(int, input().split())
K = []
S = []
for m in range(M):
    inp = list(map(int, input().split()))
    # K.append(inp[0])
    S.append(inp[1:])

P = list(map(int, input().split()))

X = []


def dfs(A):
    if N == len(A):
        X.append(A.copy())
        return
    for i in [0, 1]:
        A.append(i)
        dfs(A)
        A.pop()


dfs([])


def s(m, x):
    s = 0
    for mm in m:
        s += x[mm - 1]
    return s


count = 0
for x in X:
    flg = True  # 一つでも点灯しないものがあったらFalse
    for m, p in zip(S, P):  # 電球ループ
        su = s(m, x)
        if su % 2 != p:
            flg = False
    if flg:
        count += 1

print(count)
