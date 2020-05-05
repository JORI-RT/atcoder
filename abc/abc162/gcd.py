def my_gcd(i, j):
    if i > j:
        a = i
        b = j
    elif i == j:
        return i
    else:
        a = j
        b = i
    r = a % b

    if r == 0:
        return b
    return my_gcd(b, r)


print(my_gcd(45, 30))
