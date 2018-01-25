input_list = [0, 1, 22, 0, 5, 0, 0, 7, 10, 0, 12]

# [0, 1, 2, 0, 3] => [1, 2, 3, 0, 0]

input_len = len(input_list)
output_list = [0] * input_len
j = 0

for i in range(input_len):
    while j < input_len:
        if input_list[j] != 0:
            output_list[i] = input_list[j]
            j += 1
            break
        j += 1

print(output_list)

"""
