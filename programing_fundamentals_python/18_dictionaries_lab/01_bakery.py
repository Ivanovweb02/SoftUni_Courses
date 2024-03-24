stocks = input().split()
bakery = {}

for i in range(0, len(stocks), 2):
    food = stocks[i]
    quantity = int(stocks[i + 1])
    bakery[food] = quantity

print(bakery)
