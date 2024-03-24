data = input()

register = {}

while data != 'end':
    course_name, student_name = data.split(' : ')
    if course_name not in register:
        register[course_name] = [student_name]

    else:
        register[course_name].append(student_name)

    data = input()

for course, students in register.items():
    print(f"{course}: {len(students)}")
    print('--', '\n-- '.join(students))
