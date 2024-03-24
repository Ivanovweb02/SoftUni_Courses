command = input()
quantity_of_detergent = 0
needed_detergent = 0
counter = 0
dishes = 0
pots = 0
is_end = False

while command != "End":
    count_of_detergent = int(command)
    quantity_of_detergent += count_of_detergent * 750
    while quantity_of_detergent >= needed_detergent:
        command = input()
        if command == "End":
            is_end = True
            break
        count_of_dishes = int(command)
        counter += 1
        if counter % 3 == 0:
            needed_detergent += 15 * count_of_dishes
            pots += count_of_dishes
        else:
            needed_detergent += 5 * count_of_dishes
            dishes += count_of_dishes
    if is_end:
        break
    if quantity_of_detergent < needed_detergent:
        break

if quantity_of_detergent >= needed_detergent:
    left_detergent = quantity_of_detergent - needed_detergent
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {left_detergent} ml.")

else:
    needed_more_detergent = needed_detergent - quantity_of_detergent
    print(f"Not enough detergent, {needed_more_detergent} ml. more necessary!")
