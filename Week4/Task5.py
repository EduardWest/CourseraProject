def isPrime(n):
    if n == 1:
        return 'NO'
    if n % 2 == 0:
        if n == 2:
            return 'YES'
        else:
            return 'NO'
    d = 3
    while d * d < n and n % d != 0:
        d += 2
    if d * d > n:
        return 'YES'
    return 'NO'
n = int(input())
print(isPrime(n))
