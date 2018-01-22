list1 = [1, 8, 4, 2, 9, 5, 6, 3, 7]

list_len = len(list1)

for i in range(list_len - 1):
    list1.insert(i, list1.pop())

print(list1)

