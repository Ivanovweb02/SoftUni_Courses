count_of_orders = int(input())
price = 0
total = 0

for _ in range(count_of_orders):
    capsule_price = float(input())
    days = int(input())
    needed_capsule_per_day = int(input())
    if (capsule_price < 0.01 or capsule_price > 100.00) \
            or (days < 1 or days > 31) \
            or (needed_capsule_per_day < 1 or needed_capsule_per_day > 2000):
        continue

    price = capsule_price * needed_capsule_per_day * days
    total += price
    print(f"The price for the coffee is: ${price :.2f}")
print(f"Total: ${total :.2f}")
