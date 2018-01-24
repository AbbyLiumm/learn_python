import pprint

data = {}

def new_file_name():                                                                                    #newfile or openfile
    print("please input the file name you want to create or open (!!Note the suffix name of the file!!): ")
    i = input()
    return i

def read_file_data():                                                                                   #readfile
    read_csv = open(str(new_file_name()), "r")
    skip = read_csv.readline()

    for line in read_csv.readlines():
        new_line = line.strip()
        if new_line == "":
            continue
        words = new_line.split(",")

        data[words[0]] = {}
        person = data[words[0]]

        person["name"] = words[1]
        person["age"] = words[2]
        person["gender"] = words[3]
        person["position"] = words[4]

    pprint.pprint(data)

    read_csv.close()

def wwrite_file_data():                                                                                 #editfile
    write_csv = open(str(new_file_name()), "a")

    #----headline----#
    #write_csv.write("alias,name,age,gender,position\n")

#--------count exception handling--------#
    count = -1
    while count < 0:
        count = int(input("please input the count: "))
        if count < 0:
            print("!!WARNNING!!please input a value > 0!!!")

    for i in range(count):
        alias = input("please input alias: ")

        data[alias] = {}
        people = data[alias]

        name = input("please input name: ")
        age = input("please input age: ")
        gender = input("please input gender: ")
        position = input("please input position: ")
        people['name'] = name
        people['age'] = age
        people['gender'] = gender
        people['position'] = position

        pprint.pprint(people)

        write_csv.write(",".join([alias, name, age, gender, position]) + "\n")
        write_csv.flush()
    write_csv.close()



###--------main--------###

i = 1
pprint.pprint("1. new a file.")
pprint.pprint("2. read a file.")
pprint.pprint("3. edit a file.")
pprint.pprint("0. exit.")
while i in range(4):
    i = int(input("please input the order you want to execute: "))
    while i != 1 and i != 2 and i != 3 and i != 0:
        if i != 1 and i != 2 and i != 3 and i != 0:
            print("[!!WARNING!!] please input the right order!")
            input("please enter again: ")
    if i == 1:
        new_file_name()

    if i == 2:
        read_file_data()

    if i == 3:
        wwrite_file_data()

        print("Would you want to check the data you type-in? ")
        print("YES / NO")
        j = input()
        while j != "YES" and  j != "NO":
            if j != "YES" and j != "NO":
                print("[!!WARNING!!] please input the right option!")
                print("YES / NO")
        if j == "YES":
            read_file_data()
        else:
            pprint.pprint("Congratulations! You have entered the data successfully. ")

    if i == 0:
        break
print("Thank you for your use!")