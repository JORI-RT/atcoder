import math
import itertools

# sqrt = math.sqrt((4 - 1) ** 2 + (4 - 1) ** 2)
# print(sqrt)

N = int(input())

P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

paths = []
for one_case in itertools.permutations(P):
    sum_path = 0
    for i in range(len(P)):
        if i == len(P) - 1:
            break
        sum_path = sum_path + math.sqrt(
            (one_case[i][0] - one_case[i + 1][0]) ** 2 + (one_case[i][1] - one_case[i + 1][1]) ** 2)
    paths.append(sum_path)

print(sum(paths) / len(paths))
