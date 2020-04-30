# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_A

a = list(map(str, input().split()))


class MyStack:
    def __init__(self, data=[]):
        self.data = data

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            return "Stack is Empty"
        return self.data.pop()


def is_op(s):
    if s == '+' or s == '-' or s == '*':
        return True
    return False


def m(a):
    a2 = MyStack()
    for s in a:
        if is_op(s):
            n2 = a2.pop()
            n1 = a2.pop()
            a2.push(eval(str(n1) + s + str(n2)))
        else:
            a2.push(int(s))

    return a2


a3 = m(a)

print(a3.pop())
