stage = input()
type_of_ticket = input()
count_of_tickets = int(input())
photo_of_trophy = input()
ticket_price = 0
is_photo_free = False

if stage == "Quarter final":
    if type_of_ticket == "Standard":
        ticket_price = 55.50
    elif type_of_ticket == "Premium":
        ticket_price = 105.20
    elif type_of_ticket == "VIP":
        ticket_price = 118.90

elif stage == "Semi final":
    if type_of_ticket == "Standard":
        ticket_price = 75.88
    elif type_of_ticket == "Premium":
        ticket_price = 125.22
    elif type_of_ticket == "VIP":
        ticket_price = 300.40

elif stage == "Final":
    if type_of_ticket == "Standard":
        ticket_price = 110.10
    elif type_of_ticket == "Premium":
        ticket_price = 160.66
    elif type_of_ticket == "VIP":
        ticket_price = 400

total_price = count_of_tickets * ticket_price

if total_price > 4000:
    total_price -= total_price * 0.25
    is_photo_free = True

elif total_price > 2500:
    total_price -= total_price * 0.10

if photo_of_trophy == "Y" and not is_photo_free:
    total_price += 40 * count_of_tickets

print(f"{total_price :.2f}")
