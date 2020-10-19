from math import sqrt


def IsPointInSquare(x, y):
    return sqrt(x ** 2 + y ** 2) <= sqrt(2)
x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
