count_of_judges = int(input())
command = input()
presentation_count = 0
total_grade = 0

while command != "Finish":
    presentation_name = command
    presentation_count += 1
    current_grade = 0
    for count in range(count_of_judges):
        grades = float(input())
        current_grade += grades

    avg_grade = current_grade / count_of_judges
    print(f"{presentation_name} - {avg_grade :.2f}.")
    total_grade += current_grade

    command = input()

avg_total_grade = total_grade / (presentation_count * count_of_judges)
print(f"Student's final assessment is {avg_total_grade :.2f}.")
