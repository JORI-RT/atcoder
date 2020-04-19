import sys
a, b = map(int, input().split())


def judge(i, j, k, b):
    if 10000*i + 5000*j + 1000*k == b:
        print(str(i) + " " + str(j) + " " + str(k))
        # sys.exit()


i = 0
j = 0
k = 0
for i in range(a-j-k+1):
    print(str(i) + " " + str(j) + " " + str(k))
    judge(i, j, k, b)
    for j in range(a-i-k+1):
        print(str(i) + " " + str(j) + " " + str(k))
        judge(i, j, k, b)
        for k in range(a-i-j+1):
            print(str(i) + " " + str(j) + " " + str(k))
            judge(i, j, k, b)
