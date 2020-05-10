N, K = map(int, input().split())
A = list(map(int, input().split()))

current = 1
history = [0] * K
c = 0
first = 0
second = 0
f_flg = True
s_flg = True
for k in range(K):
    current = A[current - 1]
    history[c] = current
    c += 1
    if f_flg:
        if history.count(current) == 2:
            first = c
            f_flg = False
    if s_flg:
        if history.count(current) == 3:
            second = c
            s_flg = False
            break

print(history)
second_first = second - first + 1
print(second_first)
print(first)
print(second)
print((k - second_first) % second_first)
