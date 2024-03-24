count_of_kilometers = int(input())
day_or_night = input()
cost_per_kilometer = 0
total_cost = 0

if day_or_night == "day":
    if count_of_kilometers < 20:
        total_cost = count_of_kilometers * 0.79 + 0.70
    elif count_of_kilometers < 100:
        total_cost = count_of_kilometers * 0.09
    else:
        total_cost = count_of_kilometers * 0.06

elif day_or_night == "night":
    if count_of_kilometers < 20:
        total_cost = count_of_kilometers * 0.90 + 0.70
    elif count_of_kilometers < 100:
        total_cost = count_of_kilometers * 0.09
    else:
        total_cost = count_of_kilometers * 0.06

print(f"{total_cost:.2f}")
