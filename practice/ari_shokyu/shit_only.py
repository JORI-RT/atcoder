N = int(input())
A = list(map(int, input().split()))


def all_even(A):
    for a in A:
        if a % 2 != 0:
            return False
    return True


count = 0
while all_even(A):
    A = [i // 2 for i in A]
    count += 1

print(count)
