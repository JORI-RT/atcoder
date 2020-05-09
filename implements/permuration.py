import itertools

'''
順列の数え上げ
'''
for i in itertools.permutations([1, 2, 3]):
    print(i)

'''
実行結果
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
'''
