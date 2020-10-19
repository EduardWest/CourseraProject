inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
words = []
for line in lines:
    string = line.split()
    words.extend(string)
print(len(set(words)))
