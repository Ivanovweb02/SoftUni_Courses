sequence_of_number = input().split()
string = input()
message = ''
character = ''
new_string = string
for number in sequence_of_number:
    sum_of_digit = 0
    for current_digit in number:
        sum_of_digit += int(current_digit)

    while sum_of_digit > (len(new_string) - 1):
        sum_of_digit -= (len(new_string))

    character = new_string[sum_of_digit]
    message += character
    new_string = new_string.replace(character, '', 1)

print(message)
