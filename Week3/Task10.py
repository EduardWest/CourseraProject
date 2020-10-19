def search(task, letter, index=0, indexes=[]):
    if index == len(task):
        if len(indexes) > 1:
            return '{} {}'.format(min(indexes), max(indexes))
        elif len(indexes) == 1:
            return '{}'.format(min(indexes))
        else:
            return ''
    if task[index] == letter:
        indexes.append(index)
    return search(task, letter, index + 1)
task = input()
print(search(task, 'f'))
