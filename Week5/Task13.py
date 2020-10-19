a = list(map(int, input().split()))
max_index, min_index = a.index(max(a)), a.index(min(a))
a[max_index], a[min_index] = a[min_index], a[max_index]
print(*a)
