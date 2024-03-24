period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for current_day in range(1, period + 1):
    count_of_patient = int(input())
    if current_day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1

    if count_of_patient > doctors:
        untreated_patients += count_of_patient - doctors
        treated_patients += doctors
    else:
        treated_patients += count_of_patient

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
