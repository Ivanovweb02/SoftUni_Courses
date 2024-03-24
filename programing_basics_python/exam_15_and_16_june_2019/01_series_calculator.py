import math

serial_name = input()
season_count = int(input())
episodes_count = int(input())
episode_duration = float(input())

adds = episode_duration * 0.20
episode_duration += adds
total_time = math.floor(season_count * episodes_count * episode_duration + 10 * season_count)

print(f"Total time needed to watch the {serial_name} series is {total_time} minutes.")
