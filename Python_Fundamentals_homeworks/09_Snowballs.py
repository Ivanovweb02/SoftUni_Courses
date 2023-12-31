number_of_snow_balls = int(input())
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
best_value = 0
for snow_ball in range(number_of_snow_balls):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = int((current_weight / current_time) ** current_quality)
    if current_value > best_value:
        best_value = current_value
        snowball_weight = current_weight
        snowball_time = current_time
        snowball_quality = current_quality
print(f"{snowball_weight} : {snowball_time} = {best_value} ({snowball_quality})")
