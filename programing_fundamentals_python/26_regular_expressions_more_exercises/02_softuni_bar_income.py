import re

info = input()
total_income = 0
name_pattern = r'%([A-Z][a-z]+)%'
product_pattern = r'<([\w]+)>'
count_pattern = r'\|(\d+)\|'
price_pattern = r'([1-9]+[.0-9]*)\$'
while info != 'end of shift':
    name_match = re.search(name_pattern, info)
    product_match = re.search(product_pattern, info)
    count_match = re.search(count_pattern, info)
    price_match = re.search(price_pattern, info)
    if name_match and product_match and count_match and price_match:
        name = name_match.group(1)
        product = product_match.group(1)
        count = int(count_match.group(1))
        price = float(price_match.group(1))
        total_price = count * price
        total_income += total_price
        print(f"{name}: {product} - {total_price :.2f}")

    info = input()

print(f"Total income: {total_income :.2f}")
