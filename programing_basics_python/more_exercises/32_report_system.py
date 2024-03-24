needed_amount = int(input())
payed_with_cash = 0
payed_with_card = 0
count_of_transaction = 0
collected_amount = 0
amount_payed_by_cash = 0
amount_payed_by_card = 0
is_goal_reached = False
command = input()

while command != "End":
    sold_products = int(command)
    count_of_transaction += 1

    if count_of_transaction % 2 == 0:
        if sold_products < 10:
            command = input()
            print("Error in transaction!")
            continue
        else:
            payed_with_card += 1
            amount_payed_by_card += sold_products
    else:
        if sold_products > 100:
            command = input()
            print("Error in transaction!")
            continue
        else:
            payed_with_cash += 1
            amount_payed_by_cash += sold_products

    collected_amount += sold_products
    print("Product sold!")
    if collected_amount >= needed_amount:
        is_goal_reached = True
        break

    command = input()

if is_goal_reached:
    avg_cash_payed = amount_payed_by_cash / payed_with_cash
    avg_card_payed = amount_payed_by_card / payed_with_card
    print(f"Average CS: {avg_cash_payed :.2f}")
    print(f"Average CC: {avg_card_payed :.2f}")

else:
    print("Failed to collect required money for charity.")
