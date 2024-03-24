searched_book = input()

command = input()
checked_book = 0
is_founded = False
while command != "No More Books":
    current_book = command
    if searched_book == current_book:
        is_founded = True
        break
    command = input()
    checked_book += 1

if not is_founded:
    print("The book you search is not here!")
    print(f"You checked {checked_book} books.")
else:
    print(f"You checked {checked_book} books and found it.")
