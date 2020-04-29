# https://atcoder.jp/contests/apg4b/tasks/APG4b_v
def sumrec(i):
    if i <= 0:
        return 0
    return i + sumrec(i - 1)


def list_double(lst):
    if lst == []:
        return []
    first = lst[0]
    sss = lst[1:]
    return [first * 2] + list_double(sss)


def sum_a_b(a, b):
    if a > b:
        return 0
    return a + sum_a_b(a + 1, b)


def array_sum(array):
    if not array:
        return 0
    first = array[0]
    sss = array[1:]
    return first + array_sum(sss)


def has_divide(N, M):
    if N >= M:
        return False
    if M % (N) == 0:
        return True
    return has_divide(N + 1, M)


def is_prime(i):
    if i == 1:
        return True
    elif i == 2:
        return True
    return not (has_divide(3, i))


def reverse_array(array):
    if array == []:
        return []
    first = array[0]

# print(sumrec(5))
# print(list_double([1,1,1,2,3,4,4]))
# print(sum_a_b(int(input()), int(input())))
# print(array_sum([1, 1, 1, 3]))
# print(has_divide(2, 121))
# print(has_divide(3, 12))
# print(is_prime(109))
