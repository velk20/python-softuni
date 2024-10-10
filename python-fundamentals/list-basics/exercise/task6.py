from itertools import count

initList = input().split(' ')
initList = [int(x) for x in initList]

count = int(input())

unsortedList = list(initList)
initList.sort()

for _ in range(count):
    el = initList.pop(0)
    unsortedList.remove(el)

print(unsortedList)
