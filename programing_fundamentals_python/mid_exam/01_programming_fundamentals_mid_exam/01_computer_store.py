command = input()
computer_price = 0

while True:
    if command == 'special' or command == 'regular':
        break
    price = float(command)
    if price < 0:
        command = input()
        print('Invalid price!')
        continue
    computer_price += price
    command = input()

if computer_price > 0:
    taxes = computer_price * 0.20
    total_price = computer_price + taxes
    if command == 'special':
        total_price -= total_price * 0.10
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {computer_price :.2f}$\n"
          f"Taxes: {taxes :.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price :.2f}$")
else:
    print('Invalid order!')
