start_letter = input()
end_letter = input()
exclude_letter = input()
count = 0
for first_chart in range(ord(start_letter), ord(end_letter) + 1):
    for second_chart in range(ord(start_letter), ord(end_letter) + 1):
        for third_chart in range(ord(start_letter), ord(end_letter) + 1):
            to_print = True
            if first_chart == ord(exclude_letter) \
                    or second_chart == ord(exclude_letter) \
                    or third_chart == ord(exclude_letter):
                to_print = False
            if to_print:
                count += 1
                print(f'{chr(first_chart)}{chr(second_chart)}{chr(third_chart)}', end=" ")
print(f"{count}")
