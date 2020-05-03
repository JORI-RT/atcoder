# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_C
import hashlib

n = int(input())


# 都合のいいhash関数を定義
def h(s):
    return abs(int(str(hash(s))[:6]))


array = [0] * 1000000
for i in range(n):
    command, s = input().split()
    if command == 'insert':
        array[h(s)] = s
    if command == 'find':
        if array[h(s)] != 0:
            print('yes')
        else:
            print('no')
