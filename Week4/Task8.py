def recursive_power(a, n):
    if a == 0:
        return 0
    if n == 0:
        return 1
    if n % 2 == 0:
        return recursive_power(a ** 2, n / 2)
    else:
        return a * recursive_power(a, n - 1)
a, n = float(input()), float(input())
print(recursive_power(a, n))
