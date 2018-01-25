# give a random number, and add its digit sum


def calculate_digit_sum(num):

    if num < 0:
        print("please input a nonnegative integer: ")
        input()
    else:
        sum_digit = 0
        if num < 10:
            print("the digit sum is : " + str(num))
        else:
            while num >= 10:
                temp1 = 0
                while num > 0:
                    temp1 = int(num%10)
                    sum_digit += temp1
                    num = int(num/10)

                num = sum_digit

            print("the digit sum is : " + str(num))


# ----main---- #
print("please input a number: ")
num1 = input()

calculate_digit_sum(int(num1))
