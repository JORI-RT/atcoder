n = 5
S = [0] * n


def rec(i, S):
    if i == len(S):
        print(S)
        return
    rec(i + 1, S)

