text = "ASCII stands for American Standard Code for Information Interchange. Computers can only understand numbers, so an ASCII code is the numerical representation of a character such as 'a' or '@' or an action of some sort."

# text = text.lower()

dict1 = {}
dict1['a'] = [0, 0]
dict1['e'] = [0, 0]
dict1['i'] = [0, 0]
dict1['o'] = [0, 0]
dict1['u'] = [0, 0]

for char in text:
    c = char.lower()
    if c in dict1:
        if c == char:
            dict1[c][1] += 1
        else:
            dict1[c][0] += 1

print(dict1) 