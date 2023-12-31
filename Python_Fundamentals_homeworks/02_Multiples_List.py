factor = int(input())
count = int(input())
list_of_multiple = []
for num in range(1, count + 1):
    current_number = num * factor
    list_of_multiple.append(current_number)
print(list_of_multiple)
