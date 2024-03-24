change = float(input())

amount = int(change * 100)

coins_count = 0
while amount > 0:
    coins_count += 1

    if amount >= 200:
        amount -= 200
    elif amount >= 100:
        amount -= 100
    elif amount >= 50:
        amount -= 50
    elif amount >= 20:
        amount -= 20
    elif amount >= 10:
        amount -= 10
    elif amount >= 5:
        amount -= 5
    elif amount >= 2:
        amount -= 2
    elif amount >= 1:
        amount -= 1

print(coins_count)
