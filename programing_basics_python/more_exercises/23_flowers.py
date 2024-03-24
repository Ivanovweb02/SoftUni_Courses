chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
current_season = input()
holiday = input()

total_flowers = chrysanthemums_count + roses_count + tulips_count
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if current_season == "Spring" or current_season == "Summer":
    chrysanthemums_price = chrysanthemums_count * 2.00
    roses_price = roses_count * 4.10
    tulips_price = tulips_count * 2.50

elif current_season == "Autumn" or current_season == "Winter":
    chrysanthemums_price = chrysanthemums_count * 3.75
    roses_price = roses_count * 4.50
    tulips_price = tulips_count * 4.15

total_price = chrysanthemums_price + roses_price + tulips_price

if holiday == "Y":
    total_price += total_price * 0.15

if tulips_count > 7 and current_season == "Spring":
    total_price -= total_price * 0.05
if roses_count >= 10 and current_season == "Winter":
    total_price -= total_price * 0.10
if total_flowers > 20:
    total_price -= total_price * 0.20

total_price += 2
print(f"{total_price :.2f}")
