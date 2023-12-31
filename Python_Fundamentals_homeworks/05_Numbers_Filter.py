number = int(input())
list_of_number = []
list_of_filter_number = []
for _ in range(number):
    current_number = int(input())
    list_of_number.append(current_number)

command = input()
if command == 'even':
    for num in range(len(list_of_number)):
        if list_of_number[num] % 2 == 0:
            list_of_filter_number.append(list_of_number[num])
elif command == 'odd':
    for num in range(len(list_of_number)):
        if list_of_number[num] % 2 != 0:
            list_of_filter_number.append(list_of_number[num])
elif command == 'positive':
    for num in range(len(list_of_number)):
        if list_of_number[num] >= 0:
            list_of_filter_number.append(list_of_number[num])
elif command == 'negative':
    for num in range(len(list_of_number)):
        if list_of_number[num] < 0:
            list_of_filter_number.append(list_of_number[num])
print(list_of_filter_number)
