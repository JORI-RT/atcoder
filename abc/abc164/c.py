N = input()
N = int(N)
d = set()
for i in range(N):
    d.add(input())

print(len(d))

# set のadd の計算量とlen()の計算量