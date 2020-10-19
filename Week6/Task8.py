import sys

read = sys.stdin
n = int(read.readline())
marks = []
for line in sys.stdin:
    mark = list(map(int, line.split()[-3:]))
    if min(mark) > 39:
        marks.append(sum(mark))
if len(marks) <= n:
    print(0)
elif marks.count(max(marks)) > n:
    print(1)
else:
    marks.sort(reverse=True)
    nums = marks[:n]
    if nums[-1] == marks[n]:
        while marks[n] in nums:
            nums.remove(marks[n])
    print(min(nums))
