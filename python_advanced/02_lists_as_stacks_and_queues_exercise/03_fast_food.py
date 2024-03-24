from collections import deque

quantity_of_food = int(input())
orders = deque(input().split())
biggest_order = max([int(order) for order in orders])

while orders:
    order = int(orders.popleft())
    if quantity_of_food >= order:
        quantity_of_food -= order
    else:
        orders.appendleft(str(order))
        break

print(biggest_order)
if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(orders)}")
