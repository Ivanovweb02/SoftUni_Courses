months = int(input())
total_electricity = 0
total_water = 0
total_internet = 0
total_other_bill = 0
for _ in range(months):
    electricity_bill = float(input())
    total_electricity += electricity_bill
    water_bill = 20
    total_water += water_bill
    internet_bill = 15
    total_internet += internet_bill
    total_per_month = electricity_bill + water_bill + internet_bill
    other_bill = (total_per_month * 0.20) + total_per_month
    total_other_bill += other_bill


avg_expenses_per_month = (total_electricity + total_water + total_internet + total_other_bill) / months
print(f"Electricity: {total_electricity :.2f} lv")
print(f"Water: {total_water :.2f} lv")
print(f"Internet: {total_internet :.2f} lv")
print(f"Other: {total_other_bill :.2f} lv")
print(f"Average: {avg_expenses_per_month :.2f} lv")
