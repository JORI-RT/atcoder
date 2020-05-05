N = input()
S = sum(list(map(int, N)))

print('Yes') if int(N) % S == 0 else print('No')
