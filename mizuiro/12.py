import itertools

# bit全探索
N, M = map(int, input().split())  # N人, 関係M個
relations = [tuple(map(int, input().split())) for _ in range(M)]

for i in range(N, 0, -1):
    for j in itertools.combinations(range(1, N + 1), i):  # jは議員が何人かどうか
        if all((x, y) in relations for x, y in itertools.combinations(j, 2)):  # j人の議員から2り選ぶ組が全部relralationとあっているか
            print(i)
            break
    else:  # forの中でbreakに通らなかったらここ、flgをかかなくてよい
        continue
    break  # forでbreakに通ったあと、外のループもぬけるためにある
