budget = float(input())
category = input()
group_of_people = int(input())

ticket_price = 0
travel_expenses = 0

if category == "VIP":
    ticket_price = 499.99
    if 1 <= group_of_people <= 4:
        travel_expenses = budget * 0.75
    elif group_of_people <= 9:
        travel_expenses = budget * 0.60
    elif group_of_people <= 24:
        travel_expenses = budget * 0.50
    elif group_of_people <= 49:
        travel_expenses = budget * 0.40
    else:
        travel_expenses = budget * 0.25

elif category == "Normal":
    ticket_price = 249.99
    if 1 <= group_of_people <= 4:
        travel_expenses = budget * 0.75
    elif group_of_people <= 9:
        travel_expenses = budget * 0.60
    elif group_of_people <= 24:
        travel_expenses = budget * 0.50
    elif group_of_people <= 49:
        travel_expenses = budget * 0.40
    else:
        travel_expenses = budget * 0.25

budget_left = budget - travel_expenses
total_ticket_price = group_of_people * ticket_price

if budget_left >= total_ticket_price:
    left_money = budget_left - total_ticket_price
    print(f"Yes! You have {left_money :.2f} leva left.")
else:
    needed_money = total_ticket_price - budget_left
    print(f"Not enough money! You need {needed_money :.2f} leva.")
