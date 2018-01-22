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


christmas_tree(4)
