count_of_tab = int(input())
salary = int(input())

is_salary = True
for _ in range(1, count_of_tab + 1):
    open_websites = input()

    if open_websites == "Facebook":
        salary -= 150
    elif open_websites == "Instagram":
        salary -= 100
    elif open_websites == "Reddit":
        salary -= 50

    if salary <= 0:
        is_salary = False
        break

if is_salary:
    print(salary)
else:
    print("You have lost your salary.")

