import math
list1 = [1, 8, 4, 2, 9, 5, 6, 3, 7, 10]

list_len = len(list1)

for i in range(math.floor(list_len / 2)):               #reverse method 1
    a = list1[i]
    j = (list_len - 1) - i
    list1[i] = list1[j]
    list1[j] = a


print(list1)                                            #step
print(list1[1::2])                                      #step


print(list1[1:int(list_len/2):2])                       #reverse method 2

for i in range(list_len - 1):
    list1.insert(i, list1.pop())

print(list1)


print(list1[::-1])                                      #reverse method 3