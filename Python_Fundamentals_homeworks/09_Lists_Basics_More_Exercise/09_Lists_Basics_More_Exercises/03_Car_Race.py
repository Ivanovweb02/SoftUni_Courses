sequence_of_number = list(map(int, input().split()))

sum_of_first_car_time = 0
sum_of_second_car_time = 0
first_car = []
second_car = []

for index in range(0, int(len(sequence_of_number) / 2)):
    first_car_time = sequence_of_number[index]
    first_car.append(first_car_time)

for index in range(len(sequence_of_number) - 1, int(len(sequence_of_number) / 2), - 1):
    second_car_time = sequence_of_number[index]
    second_car.append(second_car_time)

for time in first_car:
    if time == 0:
        sum_of_first_car_time -= sum_of_first_car_time * 0.20
    sum_of_first_car_time += time

for time in second_car:
    if time == 0:
        sum_of_second_car_time -= sum_of_second_car_time * 0.20
    sum_of_second_car_time += time

winner = ''
winner_time = 0
if sum_of_first_car_time > sum_of_second_car_time:
    winner = 'right'
    winner_time = sum_of_second_car_time
else:
    winner = 'left'
    winner_time = sum_of_first_car_time

print(f"The winner is {winner} with total time: {winner_time :.1f}")
