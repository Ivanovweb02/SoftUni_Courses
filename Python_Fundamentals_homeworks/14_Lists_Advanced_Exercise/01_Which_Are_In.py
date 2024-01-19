first_sequence = input().split(', ')
second_sequence = input().split(', ')
new_list = []

for first_element in first_sequence:
    for second_element in second_sequence:
        if first_element in second_element:
            new_list.append(first_element)
            break

print(new_list)
