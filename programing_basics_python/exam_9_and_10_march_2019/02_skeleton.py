minutes = int(input())
seconds = int(input())
length = float(input())
seconds_of_100_meters = int(input())

minutes_in_seconds = minutes * 60
total_time = minutes_in_seconds + seconds
time_needed = length / 100 * seconds_of_100_meters
time_reduction = length / 120
time_reduction *= 2.5
time_needed -= time_reduction

if total_time >= time_needed:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_needed :.3f}.")

else:
    needed_time = time_needed - total_time
    print(f"No, Marin failed! He was {needed_time :.3f} second slower.")
