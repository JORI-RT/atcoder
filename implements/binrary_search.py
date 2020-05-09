'''
Arrayの中にxが含まれていたらTrueを返す
'''


def bin_search(Array, x):
    left = 0
    right = len(Array) - 1
    mid = (left + right) // 2
    while left <= right:
        if Array[mid] == x:
            return True
        if Array[mid] > x:
            right = mid - 1
        elif Array[mid] < x:
            left = mid + 1
        mid = (left + right) // 2
    return False
