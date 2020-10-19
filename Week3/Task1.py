a, b, c = float(input()), float(input()), float(input())
semi_perimetr = (a + b + c) / 2
d = semi_perimetr
print((d * (d - a) * (d - b) * (d - c)) ** 0.5)
