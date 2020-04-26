N = 2019
cnt = [0] * N
S = input()
ans = 0
for s in S:
    print(s)
    s = int(s)
    new = [0] * N
    for n in range(N):
        idx = (10 * n + s) % N
        new[idx] += cnt[n]
    cnt = new
    cnt[s] += 1
    ans += cnt[0]
# print (ans)