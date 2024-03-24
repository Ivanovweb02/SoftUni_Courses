number_of_rest_days = int(input())
number_of_working_day = 365 - number_of_rest_days
playing_time = number_of_working_day * 63 + number_of_rest_days * 127

if playing_time > 30_000:
    diff = playing_time - 30_000
    hours = diff // 60
    minutes = diff % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    diff = 30_000 - playing_time
    hours = diff // 60
    minutes = diff % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
