import math

serial_name = input()
durability_of_episode = int(input())
break_time = int(input())

lunch_time = break_time / 8
chilling_time = break_time / 4

spent_time = lunch_time + chilling_time
break_time -= spent_time

if break_time >= durability_of_episode:
    left_time = break_time - durability_of_episode
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(left_time)} minutes free time.")
else:
    needed_time = durability_of_episode - break_time
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(needed_time)} more minutes.")
