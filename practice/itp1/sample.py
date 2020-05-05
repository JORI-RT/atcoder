'''
再帰全探索のテンプレート
長さnでMの組み合わせの順列を作成する
使い方
dfs([], 4, [0, 1])
'''


def dfs(A, n, M):
    if len(A) == n:
        print(A)
        return
    for m in M:
        A.append(m)
        dfs(A, n, M)
        A.pop()


print(dfs([], 4, [0, 1]))
