photo_time = int(input())
scene_count = int(input())
scene_duration = int(input())

preparation = photo_time * 0.15
total_time = scene_count * scene_duration + preparation

if photo_time >= total_time:
    left_time = round(photo_time - total_time)
    print(f"You managed to finish the movie on time! You have {left_time} minutes left!")
else:
    needed_time = round(total_time - photo_time)
    print(f"Time is up! To complete the movie you need {needed_time} minutes.")
