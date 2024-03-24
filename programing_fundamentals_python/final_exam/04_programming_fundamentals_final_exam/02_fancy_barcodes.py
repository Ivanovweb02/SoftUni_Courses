import re

count_of_barcode = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
for _ in range(count_of_barcode):
    some_string = input()
    product_group = ''
    match = re.findall(pattern, some_string)
    if match:
        barcode = match[0]
        for char in barcode:
            if char.isdigit():
                product_group += char
        if product_group == '':
            product_group = '00'
        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
