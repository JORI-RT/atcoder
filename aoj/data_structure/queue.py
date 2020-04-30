# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_B
from collections import deque
from functools import reduce


class Element:

    def __init__(self, process, quantum):
        self.p = process
        self.q = quantum
        self.finish_time = 0

    def get_finish_time(self):
        return self.finish_time

    def get_process(self):
        return self.p

    def get_quantum(self):
        return self.q

    def elapse(self, time):
        self.q = self.q - time

    def is_finish(self, current_time):
        if self.q <= 0:
            self.finish_time = current_time - (100-self.q)
            return True
        return False


n, q = map(int, input().split())

qu = deque()
for i in range(n):
    pi, qi = map(str, input().split())
    qu.append(Element(pi, int(qi)))

result = []
time = 0
while len(qu) > 0:
    e = qu.pop()
    e.elapse(q)
    if e.is_finish(time):
        result.append(e)
    else:
        qu.append(e)
    time += 100

for i in result:
    print(i.get_process(), i.get_finish_time())
