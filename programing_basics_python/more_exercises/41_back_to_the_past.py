inheritance_money = float(input())
final_year = int(input())
spent_money = 0
years_old = 18

for period in range(1800, final_year + 1):
    current_years = years_old + (period - 1800)
    if period % 2 == 0:
        spent_money += 12_000
    else:
        spent_money += 12_000 + (current_years * 50)

if inheritance_money >= spent_money:
    money_left = inheritance_money - spent_money
    print(f"Yes! He will live a carefree life and will have {money_left :.2f} dollars left.")
else:
    needed_money = spent_money - inheritance_money
    print(f"He will need {needed_money :.2f} dollars to survive.")
