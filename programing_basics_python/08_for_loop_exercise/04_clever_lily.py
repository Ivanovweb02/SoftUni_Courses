age = int(input())
cost_of_washing_machine = float(input())
toy_price = int(input())
count_of_toys = 0
received_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        current_money = birthday * 5
        received_money += current_money
        received_money -= 1
    else:
        count_of_toys += 1
saved_money = received_money + count_of_toys * toy_price

if saved_money >= cost_of_washing_machine:
    left_money = saved_money - cost_of_washing_machine
    print(f"Yes! {left_money:.2f}")

else:
    needed_money = cost_of_washing_machine - saved_money
    print(f"No! {needed_money:.2f}")
