contract_term = input()
type_of_contract = input()
added_mobile_internet = input()
count_of_months_to_pay = int(input())
fee = 0

if contract_term == "one":
    if type_of_contract == "Small":
        fee += 9.98
    elif type_of_contract == "Middle":
        fee += 18.99
    elif type_of_contract == "Large":
        fee += 25.98
    elif type_of_contract == "ExtraLarge":
        fee += 35.99
elif contract_term == "two":
    if type_of_contract == "Small":
        fee += 8.58
    elif type_of_contract == "Middle":
        fee += 17.09
    elif type_of_contract == "Large":
        fee += 23.59
    elif type_of_contract == "ExtraLarge":
        fee += 31.79

if added_mobile_internet == "yes":
    if fee <= 10:
        fee += 5.50
    elif fee <= 30:
        fee += 4.35
    elif fee > 30:
        fee += 3.85

if contract_term == "two":
    fee -= fee * 3.75 / 100

amount_to_pay = fee * count_of_months_to_pay

print(f"{amount_to_pay :.2f} lv.")
