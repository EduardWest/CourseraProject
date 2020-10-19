def min_div(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i
n = int(input())
print(min_div(n))
