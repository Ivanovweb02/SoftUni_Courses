control_number = int(input())
counter = 0
password = ''
is_password_found = False
for first in range(1, 9 + 1):
    for second in range(1, 9 + 1):
        for third in range(1, 9 + 1):
            for fourth in range(1, 9 + 1):
                if (first < second) and (third > fourth) \
                        and (first * second) + (third * fourth) == control_number:
                    print(f'{first}{second}{third}{fourth}', end=' ')
                    counter += 1
                    if counter == 4:
                        is_password_found = True
                        password = str(first) + str(second) + str(third) + str(fourth)
print('')
if is_password_found:
    print(f'Password: {password}')
else:
    print('No!')
