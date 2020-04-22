# https://atcoder.jp/contests/arc061/tasks/arc061_a
S = input()
op_cnt = len(S) - 1
ops = []
for i in range(2 ** op_cnt):
    op = [""] * op_cnt
    for j in range(op_cnt):
        if (i >> j) & 1:
            op[j] = "+"
    ops.append(op)

# print(ops)


def eval_fomula(S, op):
    s = list(S)
    count = 1
    for i in range(len(s) - 1):
        s.insert(i+count, op[i])
        count += 1
    fomula = ""
    for k in range(len(s)):
        fomula += s[k]

    return eval(fomula)


total = 0
for i in range(2 ** op_cnt):
    total += eval_fomula(S, ops[i])

print(total)
