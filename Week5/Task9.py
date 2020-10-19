h = list(map(int, input().split(' ')))
print(*[h[i + 1] for i in range(len(h) - 1) if h[i] < h[i + 1]])
