import itertools

n, m = map(int, input().split())
relations = [tuple(map(int, input().split())) for _ in range(m)]
print(relations)

for i in range(n, 0, -1):# 大きい方からしらべる
    for j in itertools.combinations(range(1, n + 1), i):# 1C1 -> 12C2を調べる
        # 上のjは(1) (1,2), (1,2,3)とか
        if all((x, y) in relations for x, y in itertools.combinations(j, 2)):
            print(i)
            break
    else:#for の中のbreakがこなかったら入る
        continue
    break
