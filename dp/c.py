N = int(input())

costs = [[0, 0, 0] for _ in range(N + 1)]  # [[0,0,0], [10,20,30]]
for n in range(1, N + 1):
    a, b, c = map(int, input().split())
    if n == 1:
        costs[1][0] = a
        costs[1][1] = b
        costs[1][2] = c
        continue
    max_value = 0
    for i in range(3):
        if i == 0:
            tmp_max_b_a = costs[n - 1][1] + a
            tmp_max_c_a = costs[n - 1][2] + a
            max_value = max(tmp_max_b_a, tmp_max_c_a)
            costs[n][0] = max_value
        if i == 1:
            tmp_max_a_b = costs[n - 1][0] + b
            tmp_max_c_b = costs[n - 1][2] + b
            max_value = max(tmp_max_a_b, tmp_max_c_b)
            costs[n][1] = max_value
        if i == 2:
            tmp_max_a_c = costs[n - 1][0] + c
            tmp_max_b_c = costs[n - 1][1] + c
            max_value = max(tmp_max_a_c, tmp_max_b_c)
            costs[n][2] = max_value
print(max(costs[-1]))
