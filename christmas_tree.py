is_debug_mode = False

def christmas_tree(l):
    if l <= 0:
        print("Please enter the correct height of the Christmas Tree!")

    for i in range(l):
        print(" " * (l - (i + 1)) + "*" * ((i + 1)*2 - 1))   #leaves

    if (l % 2) == 0:                                         #trunk
        for m in range(int(l / 2)):
            print(" " * (l-1) + "*")
    else:
        for m in range(int(l / 2) + 1):
            print(" " * (l-1) + "*")

num = 0
if not is_debug_mode:
    word = input("provide a number of the Christmas_Tree: ")
    num = int(word)
else:
    num = 5
christmas_tree(num)