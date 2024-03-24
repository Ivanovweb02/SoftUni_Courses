count_of_number = int(input())
sum_of_even = 0
sum_of_odd = 0

for number in range(1, count_of_number + 1):
    current_number = int(input())
    if number % 2 == 0:
        sum_of_even += current_number
    else:
        sum_of_odd += current_number

if sum_of_even == sum_of_odd:
    print(f"Yes\nSum = {sum_of_even}")

else:
    difference = abs(sum_of_even - sum_of_odd)
    print(f"No\nDiff = {difference}")
