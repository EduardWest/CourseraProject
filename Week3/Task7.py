a, b, c = float(input()), float(input()), float(input())
discr = b ** 2 - 4 * a * c
if discr > 0:
    x1 = (-b - discr ** 0.5) / (2 * a)
    x2 = (-b + discr ** 0.5) / (2 * a)
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
elif discr == 0:
    x = -b / (2 * a)
    print(x)
