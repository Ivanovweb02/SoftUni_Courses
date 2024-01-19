number_of_lines = int(input())
count_of_opening_brakes = 0
count_of_closing_brakes = 0
last_sting = ''

is_balanced = True
for _ in range(number_of_lines):
    string = input()
    if (string == "(" and last_sting == "(") \
            or (string == ")" and last_sting == ")"):
        is_balanced = False
        break
    if string == '(':
        count_of_opening_brakes += 1
    elif string == ')':
        if count_of_opening_brakes == 0:
            is_balanced = False
            break
        count_of_closing_brakes += 1

    last_sting = string

if count_of_opening_brakes > 0 and count_of_opening_brakes == count_of_closing_brakes and is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
