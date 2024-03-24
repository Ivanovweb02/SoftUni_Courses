number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
student_attendance = 0
for _ in range(number_of_students):
    attendance = int(input())
    bonus = attendance / number_of_lectures * (5 + additional_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        student_attendance = attendance

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {student_attendance} lectures.")
