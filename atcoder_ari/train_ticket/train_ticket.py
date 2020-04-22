S = list(input())

ops = []
for i in range(2 ** (len(S) -1)):
    op = ["-"] * 3
    for j in range(len(S) - 1):
        if i >> j & 1:
            op[j] = "+"
    ops.append(op)

def fomula(S, op):
    s = list(S)
    count = 1
    for i in range(len(s) - 1):
        s.insert(i+count, op[i])
        count += 1
    fomula = ""
    for k in range(len(s)):
        fomula += s[k]

    return fomula


for i in range(2 ** (len(S) -1)):
    fomul = fomula(S, ops[i])
    if eval(fomul) == 7:
        print(fomul+"=7")
        exit()