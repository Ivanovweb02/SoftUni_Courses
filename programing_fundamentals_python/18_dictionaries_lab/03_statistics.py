product = input()
products = {}
while product != "statistics":
    product = product.split(": ")
    food = product[0]
    quantity = int(product[1])
    if food not in products:
        products[food] = quantity
    else:
        products[food] += quantity

    product = input()
print(f"Products in stock: ")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

total_products = len(products)
total_quantity = sum(products.values())
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
