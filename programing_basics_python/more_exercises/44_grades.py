students_taken_the_exam = int(input())
fail = 0
between = 0
average = 0
top = 0
total_grades = 0


for _ in range(1, students_taken_the_exam + 1):
    exam_grade = float(input())
    total_grades += exam_grade

    if 2.00 <= exam_grade <= 2.99:
        fail += 1
    elif exam_grade <= 3.99:
        between += 1
    elif exam_grade <= 4.99:
        average += 1
    else:
        top += 1

percent_of_top_student = top / students_taken_the_exam * 100
percent_of_avg_student = average / students_taken_the_exam * 100
percent_of_between_student = between / students_taken_the_exam * 100
percent_of_fail_student = fail / students_taken_the_exam * 100
avr_grade = total_grades / students_taken_the_exam

print(f"Top students: {percent_of_top_student :.2f}%")
print(f"Between 4.00 and 4.99: {percent_of_avg_student :.2f}%")
print(f"Between 3.00 and 3.99: {percent_of_between_student :.2f}%")
print(f"Fail: {percent_of_fail_student :.2f}%")
print(f"Average: {avr_grade :.2f}")
