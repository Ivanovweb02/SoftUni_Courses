contract_duration = input()
contract_type = input()
added_mobile_data = input()
count_months = int(input())

price_per_month = 0


if contract_duration == "one":
    if contract_type == "Small":
        price_per_month = 9.98
    elif contract_type == "Middle":
        price_per_month = 18.99
    elif contract_type == "Large":
        price_per_month = 25.98
    elif contract_type == "ExtraLarge":
        price_per_month = 35.99
elif contract_duration == "two":
    if contract_type == "Small":
        price_per_month = 8.58
    elif contract_type == "Middle":
        price_per_month = 17.09
    elif contract_type == "Large":
        price_per_month = 23.59
    elif contract_type == "ExtraLarge":
        price_per_month = 31.79

if added_mobile_data == "yes":
    if price_per_month <= 10:
        price_per_month += 5.50
    elif 10 < price_per_month <= 30:
        price_per_month += 4.35
    else:
        price_per_month += 3.85

total_price = price_per_month * count_months
if contract_duration == "two":
    total_price -= total_price * (3.75 / 100)

print(f"{total_price :.2f} lv.")
