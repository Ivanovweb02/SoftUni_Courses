hour_of_the_day = int(input())
day_of_the_week = input()

if not 10 <= hour_of_the_day <= 18 or day_of_the_week == "Sunday":
    print("closed")
else:
    print("open")
