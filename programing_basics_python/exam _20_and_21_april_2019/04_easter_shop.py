eggs_at_the_beginning = int(input())
command = input()

bought_eggs = 0
is_more_eggs_needed = False

while command != "Close":
    second_command = command
    count_of_eggs = int(input())
    if second_command == "Buy":
        if count_of_eggs > eggs_at_the_beginning:
            is_more_eggs_needed = True
            break
        else:
            bought_eggs += count_of_eggs
            eggs_at_the_beginning -= count_of_eggs
    elif second_command == "Fill":
        eggs_at_the_beginning += count_of_eggs
    command = input()

if is_more_eggs_needed:
    print(f"Not enough eggs in store!")
    print(f"You can buy only {eggs_at_the_beginning}.")
else:
    print(f"Store is closed!")
    print(f"{bought_eggs} eggs sold.")
