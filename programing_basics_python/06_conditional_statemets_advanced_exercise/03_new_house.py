type_of_flowers = input()
count_of_flowers = int(input())
budget = int(input())

flower_price = 0
discount = 0
price_increase = 0

if type_of_flowers == "Roses":
    flower_price = 5
elif type_of_flowers == "Dahlias":
    flower_price = 3.80
elif type_of_flowers == "Tulips":
    flower_price = 2.80
elif type_of_flowers == "Narcissus":
    flower_price = 3.00
elif type_of_flowers == "Gladiolus":
    flower_price = 2.50

total_cost = flower_price * count_of_flowers

if type_of_flowers == "Roses" and count_of_flowers > 80:
    discount = total_cost * 0.10
elif type_of_flowers == "Dahlias" and count_of_flowers > 90:
    discount = total_cost * 0.15
elif type_of_flowers == "Tulips" and count_of_flowers > 80:
    discount = total_cost * 0.15

if type_of_flowers == "Narcissus" and count_of_flowers < 120:
    price_increase = total_cost * 0.15
elif type_of_flowers == "Gladiolus" and count_of_flowers < 80:
    price_increase = total_cost * 0.20

final_cost = total_cost - discount + price_increase

if budget >= final_cost:
    left_amount = budget - final_cost
    print(f"Hey, you have a great garden with {count_of_flowers} {type_of_flowers} and {left_amount:.2f} leva left.")
else:
    needed_amount = final_cost - budget
    print(f"Not enough money, you need {needed_amount:.2f} leva more.")
