# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

amount_deposited = float(input())
deposit_month = int(input())
annual_interest_rate = float(input()) * 0.01
total_of_amount = amount_deposited + deposit_month * (amount_deposited * annual_interest_rate) / 12
print(total_of_amount)

