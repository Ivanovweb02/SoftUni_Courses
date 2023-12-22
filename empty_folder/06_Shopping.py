budget = int(input())
spent_amount = 0

while True:
    command = input()
    if command == 'End':
        print("You bought everything needed.")
        break
    spent_amount += int(command)
    if spent_amount > budget:
        print("You went in overdraft!")
        break
