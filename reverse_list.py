import math
list1 = [1, 8, 4, 2, 9, 5, 6, 3, 7]

list_len = len(list1)

for i in range(math.floor(list_len / 2)):
    a = list1[i]
    j = (list_len - 1) - i
    list1[i] = list1[j]
    list1[j] = a

print(list1)


for i in range(list_len - 1):
    list1.insert(i, list1.pop())

print(list1)

