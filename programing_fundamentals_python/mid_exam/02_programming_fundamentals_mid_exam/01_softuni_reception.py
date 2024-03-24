employee_capacity_1 = int(input())
employee_capacity_2 = int(input())
employee_capacity_3 = int(input())
student_count = int(input())

total_capacity_per_hour = employee_capacity_1 + employee_capacity_2 + employee_capacity_3
hour_needed = 0

while student_count > 0:
    hour_needed += 1
    if hour_needed % 4 == 0:
        continue
    student_count -= total_capacity_per_hour

print(f"Time needed: {hour_needed}h.")
