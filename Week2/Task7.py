a, b, c = int(input()), int(input()), int(input())
d = [a, b, c]
if len(d) - len(set(d)) == 0:
    print(len(d) - len(set(d)))
elif len(d) - len(set(d)) == 1:
    print(2)
else:
    print(3)
