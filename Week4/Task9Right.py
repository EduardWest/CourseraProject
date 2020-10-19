from math import gcd
n = int(input())
m = int(input())


def ReduceFraction(n, m):
    k = gcd(n, m)
    return (n//k, m//k)
print(*ReduceFraction(n, m))
