N = int(input())
ue_max = [0, 0]
sita_max = [0, 0]
migi_max = [0, 0]
hidari_max = [0, 0]
for i in range(N):
    x, y = map(int, input().split())
    if i == 0:
        ue_max[0] = x
        ue_max[1] = y
        sita_max[0] = x
        sita_max[1] = y
        migi_max[0] = x
        migi_max[1] = y
        hidari_max[0] = x
        hidari_max[1] = y
    else:
        print(x, y)
        if ue_max[1] < y:
            ue_max[0] = x
            ue_max[1] = y
        if sita_max[1] > y:
            sita_max[0] = x
            sita_max[1] = y
        if migi_max[0] < x:
            migi_max[0] = x
            migi_max[1] = y
        if hidari_max[0] > x:
            hidari_max[0] = x
            hidari_max[1] = y

print(ue_max)
print(sita_max)
print(migi_max)
print(hidari_max)

print(migi_max[0] - hidari_max[0])
