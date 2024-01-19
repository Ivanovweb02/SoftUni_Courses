initial_schedule = input().split(', ')
instruction = input()

while instruction != 'course start':
    instruction = instruction.split(':')
    command = instruction[0]
    lesson = instruction[1]
    exercise = lesson + '-Exercise'
    if command == 'Add' and lesson not in initial_schedule:
        initial_schedule.append(lesson)
    elif command == 'Insert' and lesson not in initial_schedule:
        index = int(instruction[2])
        if index < len(initial_schedule):
            initial_schedule.insert(index, lesson)
    elif command == 'Remove':
        if lesson in initial_schedule:
            initial_schedule.remove(lesson)
            if exercise in initial_schedule:
                initial_schedule.remove(exercise)
    elif command == 'Swap':
        lesson_1 = instruction[1]
        lesson_2 = instruction[2]
        exercise_2 = lesson_2 + '-Exercise'
        if lesson_1 and lesson_2 in initial_schedule:
            index_1 = initial_schedule.index(lesson_1)
            index_2 = initial_schedule.index(lesson_2)
            if exercise in initial_schedule and exercise_2 in initial_schedule:
                initial_schedule[index_1], initial_schedule[index_2] = \
                    initial_schedule[index_2], initial_schedule[index_1]
                initial_schedule.remove(exercise)
                initial_schedule.remove(exercise_2)
                initial_schedule.insert(index_2 + 1, exercise)
                initial_schedule.insert(index_1 + 1, exercise_2)
            elif exercise in initial_schedule:
                initial_schedule[index_1], initial_schedule[index_2] = \
                    initial_schedule[index_2], initial_schedule[index_1]
                initial_schedule.remove(exercise)
                initial_schedule.insert(index_2 + 1, exercise)
            elif exercise_2 in initial_schedule:
                initial_schedule[index_1], initial_schedule[index_2] = \
                    initial_schedule[index_2], initial_schedule[index_1]
                initial_schedule.remove(exercise_2)
                initial_schedule.insert(index_1 + 1, exercise_2)
            else:
                initial_schedule[index_1], initial_schedule[index_2] = \
                    initial_schedule[index_2], initial_schedule[index_1]
    elif command == 'Exercise':
        if lesson not in initial_schedule:
            if exercise not in initial_schedule:
                initial_schedule.append(lesson)
                initial_schedule.append(exercise)
        else:
            if exercise not in initial_schedule:
                digit = initial_schedule.index(lesson)
                initial_schedule.insert(digit + 1, exercise)

    instruction = input()

lesson_index = 0
for current_lesson in initial_schedule:
    lesson_index += 1
    print(f"{lesson_index}.{current_lesson}")
