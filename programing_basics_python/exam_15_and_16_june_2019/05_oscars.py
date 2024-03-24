actor_name = input()
academia_point = float(input())
assessors_count = int(input())

is_point_reached = False
for _ in range(1, assessors_count + 1):
    assessor_name = input()
    current_point = float(input())
    name_length = len(assessor_name)
    academia_point += name_length * current_point / 2
    if academia_point >= 1250.5:
        is_point_reached = True
        break

if is_point_reached:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academia_point :.1f}!")
else:
    needed_point = 1250.5 - academia_point
    print(f"Sorry, {actor_name} you need {needed_point :.1f} more!")
