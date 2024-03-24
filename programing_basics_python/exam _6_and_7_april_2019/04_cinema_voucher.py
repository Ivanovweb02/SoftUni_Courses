voucher_value = int(input())
command = input()

tickets_price = 0
tickets_count = 0
products_price = 0
other_products = 0
total_price = 0
is_voucher_passed = False

while command != "End":
    product_name = command
    length_name = len(product_name)
    left_money = voucher_value - total_price

    if length_name > 7:
        current_ticket_price = ord(product_name[0]) + ord(product_name[1])
        total_price += current_ticket_price
        if left_money >= current_ticket_price:
            tickets_count += 1
    else:
        current_products_price = ord(product_name[0])
        total_price += current_products_price
        if left_money >= current_products_price:
            other_products += 1

    if total_price > voucher_value:
        is_voucher_passed = True
        break

    command = input()

print(f"{tickets_count}")
print(f"{other_products}")
