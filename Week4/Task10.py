total = 0


def reverse(total):
    number = int(input())
    if number != 0:
        total += number
        reverse(total)
    else:
        print(total)
reverse(total)
