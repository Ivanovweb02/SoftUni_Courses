men_count = int(input())
women_count = int(input())
max_count_table = int(input())

man_number = 0
woman_number = 0

for current_man in range(1, men_count + 1):
    for current_woman in range(1, women_count + 1):
        if max_count_table == 0:
            break
        max_count_table -= 1
        print(f'({current_man} <-> {current_woman})', end=' ')
