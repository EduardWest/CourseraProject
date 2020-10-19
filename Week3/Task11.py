string = input()
low = string.find('h')
high = string.rfind('h')
print(string[:low] + string[high+1:])
