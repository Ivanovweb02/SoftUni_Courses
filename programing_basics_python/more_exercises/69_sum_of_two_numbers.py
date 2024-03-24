start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
is_founded = False
for first_number in range(start, end + 1):
    if is_founded:
        break
    for second_number in range(start, end + 1):
        counter += 1
        if first_number + second_number == magic_number:
            is_founded = True
            print(f'Combination N:{counter} ({first_number} + {second_number} = {magic_number})')
            break
if not is_founded:
    print(f'{counter} combinations - neither equals {magic_number}')
