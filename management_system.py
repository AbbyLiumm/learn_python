import pprint

data = {}

read_csv = open("data.csv", "r")
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

write_csv = open("data.csv", "a")

#write_csv.write("alias,name,age,gender,position\n")

count = -1

while count < 0:
    count = int(input("please input the count: "))
    if count < 0:
        print("!!WARNNING!!please input a value > 0!!!")

for i in range(count):
    alias = input("please input alias: ")

    data[alias] = {}
    Lewei = data[alias]

    name = input("please input name: ")
    age = input("please input age: ")
    gender = input("please input gender: ")
    position = input("please input position: ")
    Lewei['name'] = name
    Lewei['age'] = age
    Lewei['gender'] = gender
    Lewei['position'] = position

    pprint.pprint(Lewei)

    write_csv.write(",".join([alias, name, age, gender, position]) + "\n")
    write_csv.flush()

pprint.pprint(data)

write_csv.close()
