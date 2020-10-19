fIn = open('input.txt')
myDict = {}
for word in fIn.read().split():
    myDict[word] = myDict.get(word, 0) + 1
myList = sorted(myDict.items())
myList.sort(key=lambda x: x[1], reverse=True)
print(myList[0][0])
