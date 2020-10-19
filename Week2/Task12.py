x, y = int(input()), int(input())
counter = 1
while True:
    if x >= y:
        break
    x *= 1.1
    counter += 1
print(counter)
