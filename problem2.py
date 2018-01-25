# give a random number, and calculate its digit sum


def calculate_digit_sum(num):
    num_len = len(str(num))
    sum_digit = 0
    if num_len == 0:
        sum_digit = num
        print("the digit sum is : " + sum_digit)
    else:
        for i in num_len:
            temp1 = int(num % 10)
            sum_digit += temp1
            num = (num - temp1) / 10

    print(sum_digit)



num1 = input("please input a number: ")

calculate_digit_sum(num1)
