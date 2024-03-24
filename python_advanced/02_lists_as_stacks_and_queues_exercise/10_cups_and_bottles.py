from collections import deque

capacity_of_cups = deque(list(map(int, input().split())))
capacity_of_bottles = list(map(int, input().split()))
wasted_water = 0

while capacity_of_bottles and capacity_of_cups:
    current_cup = capacity_of_cups.popleft()
    current_bottle = capacity_of_bottles.pop()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        capacity_of_cups.appendleft(current_cup)

if capacity_of_bottles:
    print('Bottles:', end=' ')
    while len(capacity_of_bottles) != 1:
        print({capacity_of_bottles.pop()}, end=' ')
    print(capacity_of_bottles.pop())
else:
    print('Cups:', end=' ')
    while len(capacity_of_cups) != 1:
        print(capacity_of_cups.popleft(), end=' ')
    print(capacity_of_cups.popleft())
print(f"Wasted litters of water: {wasted_water}")
