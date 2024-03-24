people = int(input())
lift_state = list(map(int, input().split()))
index = 0
is_done = False
while True:
    if is_done:
        break

    if people >= 4:
        entered_people = 4 - lift_state[index]
        lift_state[index] += entered_people
        people -= entered_people
    else:
        left_people = (4 - lift_state[index])
        if left_people > people:
            lift_state[index] += people
            people -= people
        else:
            people -= left_people
            lift_state[index] += left_people

    index += 1
    if people == 0 and sum(lift_state) < len(lift_state) * 4:
        is_done = True
        print(f"The lift has empty spots!")
        print(*lift_state)
    elif people > 0 and sum(lift_state) == len(lift_state) * 4:
        is_done = True
        print(f"There isn't enough space! {people} people in a queue!")
        print(*lift_state)
    elif people == 0 and sum(lift_state) == len(lift_state) * 4:
        is_done = True
        print(*lift_state)
