needed_money = float(input())
money_on_hand = float(input())

days = 0
days_of_spending = 0

while money_on_hand < needed_money:
    type_of_action = input()    # spend or save
    amount_of_money = float(input())
    days += 1

    if type_of_action == "save":
        money_on_hand += amount_of_money
        days_of_spending = 0
    elif type_of_action == "spend":
        money_on_hand -= amount_of_money
        days_of_spending += 1
        if money_on_hand < 0:
            money_on_hand = 0
    if days_of_spending >= 5:
        break


if money_on_hand >= needed_money:
    print(f"You saved the money for {days} days.")

if days_of_spending == 5:
    print("You can't save the money.")
    print(f"{days}")
