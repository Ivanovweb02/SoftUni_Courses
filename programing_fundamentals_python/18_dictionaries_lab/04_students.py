student_data = input()

students = []
while ":" in student_data:
    name, id_data, course = student_data.split(':')

    students.append({'name': name, 'id_data': id_data, 'course': course})
    student_data = input()

search_course = student_data
for student in students:
    if search_course.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['id_data']}")
