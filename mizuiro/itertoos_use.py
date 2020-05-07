import itertools

relations = [(1, 2), (2, 3), (1, 3)]

print(relations)

# for j in itertools.combinations(range(5), 2):
#     print(j)

for i in itertools.combinations((1, 2, 3, 4, 5), 2):
    print(i)

# [print((x, y)) in relations for x, y in itertools.combinations(range(4), 2)]
