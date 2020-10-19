n = int(input())
a = list(map(int, input().split()))
find_num = int(input())
print(min((abs(find_num - i), i) for i in a)[1])
