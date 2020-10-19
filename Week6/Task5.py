a = open('input.txt', 'r', encoding='utf8')
b = open('output.txt', 'w', encoding='utf8')
m = []
for line in a:
    m.append(line.split())
m.sort()
for i in range(len(m)):
    print(*m[i][:2], m[i][3], file=b)
a.close()
b.close()
