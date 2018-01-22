def get_second_num(alist):
    if len(alist) < 2:
        print("an error occur")
        return -1
    num = alist[1]
    return num

# get the diff from the two number 
def get_diff(char, tmp):
    if len(char) != 1 or len(tmp) != 1:   # check if 
        return 0
    diff = int(char) - int(tmp)
    if diff <= 0:
        return 0
    return diff

#what_is_range = range(5)

lewei_phone = "15910827825"
tmp = "33"

sum_number = 0
for index in range(len(lewei_phone)):
    char = lewei_phone[index]
    sum_number += get_diff(char, tmp)

sum_number2 = 0
for char in lewei_phone:
    sum_number2 += get_diff(char, tmp)
    

abby_list = [1]
abby_list.append('i')
abby_list.append(3)

diff = int('3') - int('0')

isTrue = 3 == '3'

abby_list.append('3')
length = len(abby_list)
second_num = get_second_num(abby_list)