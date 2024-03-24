aluminum_count = int(input())
aluminum_type = input()
way_to_receive = input()

price = 0

if aluminum_type == '90X130':
    price = 110
    if 30 < aluminum_count <= 60:
        price -= price * 0.05
    elif 60 < aluminum_count:
        price -= price * 0.08
elif aluminum_type == '100X150':
    price = 140
    if 40 < aluminum_count <= 80:
        price -= price * 0.06
    elif 80 < aluminum_count:
        price -= price * 0.10
elif aluminum_type == '130X180':
    price = 190
    if 20 < aluminum_count <= 50:
        price -= price * 0.07
    elif 50 < aluminum_count:
        price -= price * 0.12
elif aluminum_type == '200X300':
    price = 250
    if 25 < aluminum_count <= 50:
        price -= price * 0.09
    elif 50 < aluminum_count:
        price -= price * 0.14

total_cost = price * aluminum_count
if way_to_receive == 'With delivery':
    total_cost += 60
if aluminum_count > 99:
    total_cost -= total_cost * 0.04

if aluminum_count < 10:
    print("Invalid order")
else:
    print(f"{total_cost :.2f} BGN")
