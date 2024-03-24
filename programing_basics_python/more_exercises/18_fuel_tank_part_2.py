type_of_fuel = input()
quantity_of_fuel = float(input())
discount_card = input()
discount = 0
cost_of_fuel = 0

if type_of_fuel == "Gasoline":
    cost_of_fuel = quantity_of_fuel * 2.22
    if discount_card == "Yes":
        discount = 0.18 * quantity_of_fuel
elif type_of_fuel == "Diesel":
    cost_of_fuel = quantity_of_fuel * 2.33
    if discount_card == "Yes":
        discount = 0.12 * quantity_of_fuel
elif type_of_fuel == "Gas":
    cost_of_fuel = quantity_of_fuel * 0.93
    if discount_card == "Yes":
        discount = 0.08 * quantity_of_fuel

final_price = cost_of_fuel - discount

if 20 <= quantity_of_fuel <= 25:
    final_price -= final_price * 0.08
elif quantity_of_fuel > 25:
    final_price -= final_price * 0.10

print(f"{final_price:.2f} lv.")
