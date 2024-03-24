budget = float(input())
command = input()

total_price = 0
count_of_product = 0
is_passed = False

while command != "Stop":
    product_name = command
    product_price = float(input())
    count_of_product += 1
    if count_of_product % 3 == 0:
        product_price /= 2
    total_price += product_price
    if total_price > budget:
        is_passed = True
        break
    command = input()

if is_passed:
    needed_money = total_price - budget
    print("You don't have enough money!")
    print(f"You need {needed_money :.2f} leva!")
else:
    print(f"You bought {count_of_product} products for {total_price :.2f} leva.")
