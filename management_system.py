data = {}

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

print(data)