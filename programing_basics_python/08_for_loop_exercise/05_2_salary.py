count_of_tab = int(input())
salary = int(input())

for _ in range(1, count_of_tab + 1):
    open_websites = input()
    if open_websites == "Facebook":
        salary -= 150
    elif open_websites == "Instagram":
        salary -= 100
    elif open_websites == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
