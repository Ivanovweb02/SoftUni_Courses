actor_name = input()
points = float(input())
number_of_assessors = int(input())


for _ in range(number_of_assessors):
    assessor_name = input()
    point_from_assessor = float(input())
    current_point = len(assessor_name) * point_from_assessor / 2
    points += current_point

    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break

else:
    needed_point = 1250.5 - points
    print(f"Sorry, {actor_name} you need {needed_point:.1f} more!")
