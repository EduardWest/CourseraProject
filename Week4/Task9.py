m, n = int(input()), int(input())


def NOD(a, b):
    if b > a:
        a, b = b, a
    if a == b:
        return a
    return NOD(b, a - b)


def ReduceFraction():
    divider = NOD(m, n)
    return (int(m / divider), int(n / divider))
print(*ReduceFraction())
