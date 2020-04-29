N = int(input())
input = list(map(int, input().split()))

ary = [[]] * N

for i in range(N):
    l = []
    for j in range(len(input)):
        if i == input[j]:
            l.append(j)
    ary[i] = l

print(ary)


def re(array, i):
    if array[i] == []:
        return 1
    num_i = 0
    for j in array[i]:
        num_i = num_i + re(array[i], j)
    num_i + 1
    return num_i


for k in range(N):
    print(re(ary[k], k))
