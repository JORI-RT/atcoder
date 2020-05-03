# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_A
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

C = 0
for t in T:
    for s in S:
        if s == t:
            C = C + 1
            break

print(C)
