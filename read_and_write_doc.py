#read_doc = open('lesson1.py', 'r')

#print("".join(read_doc.readlines()[1::2]))
'''
write_doc = open('Abby.txt', 'w')

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

    write_doc.write("\n\naabb\n")
    write_doc.write(str(Lewei) + "\n")

write_doc.write(str(data))

write_csv = open("data.csv", "w")

write_csv.write("name,age,gender,position\n")
write_csv.write("lewlu,Lewei,26,male,rsde\n")
write_csv.write("Peiyun,22,female,intern\n")

write_csv.flush()

write_csv.close()
'''
read_csv = open("data.csv", "r")
line = read_csv.readline()
line = read_csv.readline()

words = line.split(',')
person = {}

person['name'] = words[0]
print(line)
print(words)
