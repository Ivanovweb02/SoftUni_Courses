budget = float(input())
command = input()
total_amount = 0
count_of_product = 0
is_budget_passed = False
while command != "Stop":
    name_of_product = command
    price_of_product = float(input())
    count_of_product += 1
    if count_of_product % 3 == 0:
        price_of_product /= 2
    total_amount += price_of_product
    if total_amount > budget:
        is_budget_passed = True
        break
    command = input()

if is_budget_passed:
    needed_money = total_amount - budget
    print(f"You don't have enough money!")
    print(f"You need {needed_money :.2f} leva!")

else:
    print(f"You bought {count_of_product} products for {total_amount :.2f} leva.")
