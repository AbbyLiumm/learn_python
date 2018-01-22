import random
import time
from datetime import datetime

def convert_int_to_order_name(num):
    order_name = ""
    if num == 1:
        order_name = "first"
    elif num == 2:
        order_name = "second"
    elif num == 3:
        order_name = "third"
    elif num == 4:
        order_name = "fourth"
    elif num == 5:
        order_name = "fifth"
    else:
        order_name = "error"

    return order_name

sum = 0

MAX_NUM = 10

for i in range(5):
    print("I'm Abby")
    print("I'm Lewei")
    minute = datetime.today().minute
    second = datetime.today().second
    rand = random.randint(1, 100)
    order_name = convert_int_to_order_name(i + 1)
    print("generate {0} random number({1}) at {2}:{3}".format(order_name, rand, minute, second))
    sum = sum + rand

print("sum of random is " + str(sum))
