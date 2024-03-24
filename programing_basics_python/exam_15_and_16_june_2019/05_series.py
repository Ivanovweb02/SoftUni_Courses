budget = float(input())
serial_count = int(input())

total_price = 0

for _ in range(1, serial_count + 1):
    serial_name = input()
    serial_price = float(input())
    if serial_name == "Thrones":
        serial_price -= serial_price * 0.50
    elif serial_name == "Lucifer":
        serial_price -= serial_price * 0.40
    elif serial_name == "Protector":
        serial_price -= serial_price * 0.30
    elif serial_name == "TotalDrama":
        serial_price -= serial_price * 0.20
    elif serial_name == "Area":
        serial_price -= serial_price * 0.10

    total_price += serial_price

if total_price > budget:
    needed_amount = total_price - budget
    print(f"You need {needed_amount :.2f} lv. more to buy the series!")
else:
    left_amount = budget - total_price
    print(f"You bought all the series and left with {left_amount :.2f} lv.")
