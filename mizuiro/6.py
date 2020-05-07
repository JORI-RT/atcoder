import itertools

N = int(input())
S = input()

count = 0
res = []
for i in itertools.combinations(list(S), 3):
    if i in res:
        continue
    else:
        count += 1
        res.append(i)
print(len(res))
