# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_A

a = list(map(str, input().split()))


def is_op(s):
    if s == '+' or s == '-' or s == '*':
        return True
    return False


a2 = []
for s in a:
    if is_op(s):
        n2 = a2.pop()
        n1 = a2.pop()
        a2.append(eval(str(n1) + s + str(n2)))
    else:
        a2.append(int(s))

print(a2.pop())
