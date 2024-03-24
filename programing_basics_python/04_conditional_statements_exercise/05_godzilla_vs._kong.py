movie_budget = float(input())
count_of_extras = int(input())
price_for_clothing_of_one_extra = float(input())

set_for_movie = movie_budget * 0.1
movie_budget -= set_for_movie

if count_of_extras > 150:
    discount = price_for_clothing_of_one_extra * 0.1
    price_for_clothing_of_one_extra -= discount

if count_of_extras * price_for_clothing_of_one_extra > movie_budget:
    not_enough_money = count_of_extras * price_for_clothing_of_one_extra - movie_budget
    print(f"Not enough money!\nWingard needs {not_enough_money:.2f} leva more.")

if count_of_extras * price_for_clothing_of_one_extra <= movie_budget:
    left_money = movie_budget - count_of_extras * price_for_clothing_of_one_extra
    print(f"Action!\nWingard starts filming with {left_money:.2f} leva left.")
