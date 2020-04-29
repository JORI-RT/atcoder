N = int(input())
S = input()

count = 0
for i in range(N):
    rgb_i = S[i]
    for j in range(i, N):
        rgb_j = S[j]
        if rgb_i == rgb_j:
            continue
        for k in range(j, N):
            rgb_k = S[k]
            if rgb_k == rgb_j or rgb_k == rgb_i:
                continue
            if j-i == k -j:
                continue
            count += 1

print(count)
