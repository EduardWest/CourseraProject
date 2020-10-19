p, x, y = int(input()), int(input()), int(input())
percent = 1 + p / 100
summa = x + y / 100
rubl = int(summa * percent)
cent = int(round((summa * percent - rubl) * 100, 2))
print(rubl, cent)
