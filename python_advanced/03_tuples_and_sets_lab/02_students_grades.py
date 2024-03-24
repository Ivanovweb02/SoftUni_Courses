numbers_of_students = int(input())
students_dict = {}

for _ in range(numbers_of_students):
    name, grade = tuple(input().split())
    grade = float(grade)
    if name not in students_dict.keys():
        students_dict[name] = []
    students_dict[name].append(grade)

for student_name, value in students_dict.items():
    result = ' '.join([f"{grade :.2f}" for grade in students_dict[student_name]])
    print(f"{student_name} -> {result} (avg: {sum(students_dict[student_name]) / len(students_dict[student_name]) :.2f})")
