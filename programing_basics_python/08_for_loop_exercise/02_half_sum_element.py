import sys

count_of_number = int(input())
total_sum = 0
max_number = -sys.maxsize
for number in range(count_of_number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total_sum += current_number

if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    difference = abs(total_sum - max_number * 2)
    print(f"Diff = {difference}")
