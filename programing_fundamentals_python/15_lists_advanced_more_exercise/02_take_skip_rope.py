some_string = input()
number_list = []
non_number_list = []
result_string = ""
take_string = ""
skip_string = ""

for character in some_string:
    if character.isnumeric():
        number_list.append(character)
    else:
        non_number_list.append(character)

take_list = []
skip_list = []
for index in range(len(number_list)):
    if index % 2 == 0:
        take_list.append(number_list[index])
    else:
        skip_list.append(number_list[index])

count = 0
take_index = 0
skip_index = 0
while True:
    if count % 2 == 0:
        if take_index >= len(take_list):
            break
        current_index = int(take_list[take_index])
        if current_index > len(non_number_list):
            break
        for take in range(current_index):
            take_string += non_number_list[take]
        for _ in range(current_index):
            non_number_list.pop(0)
        take_index += 1
        count += 1
    else:
        if skip_index >= len(skip_list):
            break
        current_index = int(skip_list[skip_index])
        if current_index > len(non_number_list):
            break
        for skip in range(current_index):
            skip_string += non_number_list[skip]
        for _ in range(current_index):
            non_number_list.pop(0)
        skip_index += 1
        count += 1


result_string = take_string
print(result_string)
