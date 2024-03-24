# name_of_student = input()
# grade = 0
# annual_mark = 0
#
# while grade != 12:
#     student_mark = float(input())
#     annual_mark += student_mark
#     grade += 1
#     if student_mark < 4.00:
#         print(f"{name_of_student} has been excluded at {grade} grade")
#         break
#
# average_mark = annual_mark / grade
# if grade == 12:
#     print(f"{name_of_student} graduated. Average grade: {average_mark:.2f}")

student = input()
total_grade = 0
bad_attempts = 0
current_class = 1
is_excluded = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_attempts += 1
        if bad_attempts > 1:
            is_excluded = True
            break
        continue
    current_class += 1
    total_grade += current_grade
if is_excluded:
    print(f"{student} has been excluded at {current_class} grade")
else:
    average_grade = total_grade / 12
    print(f"{student} graduated. Average grade: {average_grade:.2f}")
