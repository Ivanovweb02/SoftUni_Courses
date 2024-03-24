# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
import math

record = float(input())
distance = float(input())
time_in_second_per_meter = float(input())

total_time = distance * time_in_second_per_meter
slowdown_by_water_resistance = math.floor(distance/15) * 12.5
total_time += slowdown_by_water_resistance

if record > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    missing_seconds = total_time - record
    print(f"No, he failed! He was {missing_seconds:.2f} seconds slower.")
