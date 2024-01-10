version = input().split('.')

first_digit = version[0]
second_digit = version[1]
third_digit = version[2]
next_version = []

current_version = first_digit + second_digit + third_digit
update = int(current_version) + 1

for digit in str(update):
    next_version.append(digit)

result = '.'.join(next_version)
print(result)
