X = int(input())
mony = 100

keika_nen = 0
while True:
    keika_nen += 1
    mony = int(1.01 * mony)
    if mony >= X:
        break

print(keika_nen)
