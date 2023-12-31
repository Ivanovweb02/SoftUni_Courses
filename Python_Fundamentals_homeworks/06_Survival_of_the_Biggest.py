number = input().split(' ')
count_of_remove = int(input())
list_of_left_numbers = []

for current_index in range(len(number)):
    current_number = int(number[current_index])
    list_of_left_numbers.append(current_number)
for _ in range(count_of_remove):
    list_of_left_numbers.remove(min(list_of_left_numbers))

print(str(list_of_left_numbers)[1:-1])
