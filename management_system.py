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

print(data)

read_csv.close()

write_csv = open("data.csv", "a")

#write_csv.write("alias,name,age,gender,position\n")

for i in range(3):
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

    print(Lewei)

    write_csv.write(",".join([alias, name, age, gender, position]) + "\n")
    write_csv.flush()

print(data)

write_csv.close()
