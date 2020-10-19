a = list(map(int, input().split()))
d = max(a)
s2 = len(a)
s = a.reverse()
s1 = a.index(d)
s3 = s2 - s1 - 1
print(d, s3)
