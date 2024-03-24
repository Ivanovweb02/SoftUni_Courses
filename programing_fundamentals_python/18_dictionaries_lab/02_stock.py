products = input().split()
inventory = {}

for i in range(0, len(products), 2):
    food = products[i]
    quantity = int(products[i + 1])
    inventory[food] = quantity

search_products = input().split()

for product in search_products:
    if product in inventory:
        print(f"We have {inventory[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
