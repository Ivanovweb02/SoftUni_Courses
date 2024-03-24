def fill_the_box(height, length, width, *quantity):
    total_space = height * length * width

    for el in quantity:
        if el == 'Finish':
            break
        total_space -= el

    if total_space >= 0:
        return f"There is free space in the box. You could put {total_space} more cubes."
    else:
        return f"No more free space! You have {abs(total_space)} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
