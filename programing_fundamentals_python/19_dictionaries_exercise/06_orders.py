items = input()
products = {}

while items != 'buy':
    name, price, quantity = items.split()
    price, quantity = float(price), int(quantity)

    quantity_left = 0
    if name not in products:
        products[name] = {}
        products[name][price] = 0
    else:
        quantity_left = list(products[name].values())
        quantity_left = quantity_left[0]
        products[name].clear()
        products[name] = {}
        products[name][price] = 0

    products[name][price] += quantity + quantity_left
    items = input()

for item in products:
    for (price, quantity) in products[item].items():
        total_price = price * quantity
        print(f"{item} -> {total_price :.2f}")
