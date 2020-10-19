string = input()
if string.find('f') == -1:
    print(-2)
elif string.find('f') == string.rfind('f'):
    print(-1)
else:
    print(string[string.find('f')+1:].find('f') + string.find('f') + 1)
