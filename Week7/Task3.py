a, b = list(map(int, input().split())), set()
for i in a:
    if i in b:
        print('YES')
    else:
        print('NO')
        b.add(i)
