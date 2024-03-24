import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

slowdown = math.floor(distance_in_meters / 50)
current_time = time_in_seconds * distance_in_meters + slowdown * 30

diff = abs(record_in_seconds - current_time)

if current_time < record_in_seconds:
    print(f" Yes! The new record is {current_time :.2f} seconds.")
else:
    diff = current_time - record_in_seconds
    print(f"No! He was {diff :.2f} seconds slower.")
