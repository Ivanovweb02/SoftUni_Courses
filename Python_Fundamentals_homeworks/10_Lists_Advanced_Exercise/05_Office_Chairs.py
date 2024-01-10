number_of_rooms = int(input())
total_chairs = 0
are_chairs_enough = True

for current_room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    if chairs >= visitors:
        total_chairs += (chairs - visitors)
    else:
        needed_chairs = visitors - chairs
        are_chairs_enough = False
        print(f"{needed_chairs} more chairs needed in room {current_room}")

if are_chairs_enough:
    print(f"Game On, {total_chairs} free chairs left")
