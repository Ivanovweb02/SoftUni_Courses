from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque(int(x) for x in input().split(', '))

milk_shake = 0
while chocolate and milk:
    if milk_shake == 5:
        break
    curr_chocolate = chocolate.pop()
    curr_milk = milk.popleft()
    if curr_chocolate > 0 and curr_milk > 0:
        if curr_chocolate == curr_milk:
            milk_shake += 1
        else:
            curr_chocolate -= 5
            chocolate.append(curr_chocolate)
            milk.append(curr_milk)
    else:
        if curr_chocolate > 0:
            chocolate.append(curr_chocolate)
        elif curr_milk > 0:
            milk.appendleft(curr_milk)

if milk_shake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(num) for num in chocolate) or 'empty'}")

print(f"Milk: {', '.join(str(num) for num in milk) or 'empty'}")
