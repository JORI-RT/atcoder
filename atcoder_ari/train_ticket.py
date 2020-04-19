# https://atcoder.jp/contests/abc079/tasks/abc079_c
import random
import sys

str = input()


def retop():
    if(random.uniform(0, 1) > 0.5):
        return "+"
    return "-"


for i in range(100):
    formula = (str[0] + retop() + str[1] + retop() + str[2] + retop() + str[3])
    if eval(formula) == 7:
        print(formula + "=7")
        sys.exit()
