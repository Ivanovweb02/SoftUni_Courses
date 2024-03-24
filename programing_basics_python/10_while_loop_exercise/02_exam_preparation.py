count_of_bed_grades = int(input())
total_bed_grades = 0
total_grades = 0
count_of_problems = 0
name_of_last_problem = ""

command = input()
while command != "Enough":
    problem_name = command
    grade = int(input())

    name_of_last_problem = problem_name
    total_grades += grade
    count_of_problems += 1

    if grade <= 4:
        total_bed_grades += 1
        if count_of_bed_grades == total_bed_grades:
            break
    command = input()

average_score = total_grades / count_of_problems

if command == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {count_of_problems}")
    print(f"Last problem: {name_of_last_problem}")

else:
    print(f"You need a break, {count_of_bed_grades} poor grades.")
