list_of_lessons = input().split(', ')
instruction = input()

while instruction != 'course start':
    instruction = instruction.split(':')
    command = instruction[0]
    lesson = instruction[1]
    exercise = lesson + '-Exercise'

    if command == 'Add' and lesson not in list_of_lessons:
        list_of_lessons.append(lesson)
    elif command == 'Insert' and lesson not in list_of_lessons:
        index = int(instruction[2])
        list_of_lessons.insert(index, lesson)
    elif command == 'Remove' and lesson in list_of_lessons:
        if exercise not in list_of_lessons:
            list_of_lessons.remove(lesson)
        else:
            list_of_lessons.remove(lesson)
            list_of_lessons.remove(exercise)
    elif command == 'Swap':
        lesson_1 = instruction[1]
        lesson_2 = instruction[2]
        exercise_2 = lesson_2 + '-Exercise'
        if (lesson_1 and lesson_2) in list_of_lessons:
            if exercise in list_of_lessons and exercise_2 in list_of_lessons:
                index_1 = list_of_lessons.index(lesson_1)
                index_2 = list_of_lessons.index(lesson_2)
                list_of_lessons[index_1], list_of_lessons[index_2] = \
                    list_of_lessons[index_2], list_of_lessons[index_1]
                list_of_lessons.remove(exercise)
                list_of_lessons.remove(exercise_2)
                list_of_lessons.insert(index_2, exercise)
                list_of_lessons.insert(index_1, exercise_2)

            elif exercise in list_of_lessons:
                index_1 = list_of_lessons.index(lesson_1)
                index_2 = list_of_lessons.index(lesson_2)
                list_of_lessons[index_1], list_of_lessons[index_2] = \
                    list_of_lessons[index_2], list_of_lessons[index_1]
                list_of_lessons.remove(exercise)
                list_of_lessons.insert(index_2 + 1, exercise)
            elif exercise_2 in list_of_lessons:
                index_1 = list_of_lessons.index(lesson_1)
                index_2 = list_of_lessons.index(lesson_2)
                list_of_lessons[index_1], list_of_lessons[index_2] = \
                    list_of_lessons[index_2], list_of_lessons[index_1]
                list_of_lessons.remove(exercise_2)
                list_of_lessons.insert(index_1 + 1, exercise_2)
            else:
                index_1 = list_of_lessons.index(lesson_1)
                index_2 = list_of_lessons.index(lesson_2)
                list_of_lessons[index_1], list_of_lessons[index_2] = \
                    list_of_lessons[index_2], list_of_lessons[index_1]

    elif command == 'Exercise':
        if lesson in list_of_lessons and exercise not in list_of_lessons:
            index = list_of_lessons.index(lesson)
            list_of_lessons.insert((index + 1), exercise)
        elif lesson not in list_of_lessons and exercise not in list_of_lessons:
            list_of_lessons.append(lesson)
            list_of_lessons.append(exercise)
    instruction = input()

lesson_counter = 0
for current_lesson in list_of_lessons:
    lesson_counter += 1
    print(f"{lesson_counter}.{current_lesson}")
