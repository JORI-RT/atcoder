X = int(input())

for i in range(-130, 130):
    for j in range(-130, 130):
        if X == i ** 5 - j ** 5:
            print(i, j)
            exit()
