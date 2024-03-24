count_of_rows = int(input())
diary = {}

for _ in range(count_of_rows):
    name = input()
    grade = float(input())
    if name not in diary:
        diary[name] = [grade]
    else:
        diary[name].append(grade)

for student, grades in diary.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade :.2f}")
