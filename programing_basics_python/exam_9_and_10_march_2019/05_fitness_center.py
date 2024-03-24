count_of_visitors = int(input())
back = 0
chest = 0
legs = 0
abdominal = 0
protein_shake = 0
protein_bar = 0

for _ in range(1, count_of_visitors + 1):
    fitness_activity = input()
    if fitness_activity == "Back":
        back += 1
    elif fitness_activity == "Chest":
        chest += 1
    elif fitness_activity == "Legs":
        legs += 1
    elif fitness_activity == "Abs":
        abdominal += 1
    elif fitness_activity == "Protein shake":
        protein_shake += 1
    elif fitness_activity == "Protein bar":
        protein_bar += 1

work_out = back + chest + legs + abdominal
protein = protein_shake + protein_bar
percent_work_out = (work_out / count_of_visitors) * 100
percent_protein = (protein / count_of_visitors) * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abdominal} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percent_work_out :.2f}% - work out")
print(f"{percent_protein :.2f}% - protein")
