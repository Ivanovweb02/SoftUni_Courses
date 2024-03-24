client_count = int(input())
total_amount = 0

for _ in range(1, client_count + 1):
    command = input()
    price = 0
    count_purchase = 0

    while command != "Finish":
        purchase = command
        count_purchase += 1
        if purchase == "basket":
            price += 1.50
        elif purchase == "wreath":
            price += 3.80
        elif purchase == "chocolate bunny":
            price += 7
        command = input()

    if count_purchase % 2 == 0:
        price -= price * 0.20
    total_amount += price
    print(f"You purchased {count_purchase} items for {price :.2f} leva.")

avg_amount = total_amount / client_count
print(f"Average bill per client is: {avg_amount :.2f} leva.")
