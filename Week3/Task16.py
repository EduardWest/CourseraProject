import re
string = input()
mystr = re.sub(r"@", "", string)
print(mystr)
