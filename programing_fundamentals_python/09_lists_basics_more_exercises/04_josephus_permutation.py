list_of_numbers = input().split()
key_number = int(input())
list_of_executed = []
counter = 0

index = 0
while len(list_of_numbers) > 0:
    counter += 1
    if counter % key_number == 0:
        list_of_executed.append(list_of_numbers[index])
        list_of_numbers.pop(index)
    else:
        index += 1

    if index >= len(list_of_numbers):
        index = 0

print(str(list_of_executed).replace(' ', '').replace('\'', ''))
