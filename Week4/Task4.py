from math import sqrt, ceil


def MinDivisor(n):
    for divide in range(2, ceil(sqrt(n)) + 1):
        if n % divide == 0:
            return divide
    return n
n = int(input())
print(MinDivisor(n))
