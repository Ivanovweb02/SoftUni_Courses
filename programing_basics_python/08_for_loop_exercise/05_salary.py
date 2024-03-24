count_of_tab = int(input())
salary = int(input())
fine = 0

for _ in range(1, count_of_tab + 1):
    open_websites = input()
    if open_websites == "Facebook":
        fine += 150
    elif open_websites == "Instagram":
        fine += 100
    elif open_websites == "Reddit":
        fine += 50

left_salary = salary - fine

if left_salary <= 0:
    print("You have lost your salary.")

else:
    print(left_salary)
