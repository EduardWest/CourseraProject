a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
detA = a * d - b * c
detB1 = e * d - b * f
detB2 = a * f - e * c
print(detB1 / detA, detB2 / detA)
