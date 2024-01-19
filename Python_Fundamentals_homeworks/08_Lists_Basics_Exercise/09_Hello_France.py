collection_of_items = input().split('|')
budget = float(input())
train_ticket = 150
list_of_bought_items = []
spent_money = 0
sum_of_bought_items = 0
for item in collection_of_items:
    args = item.split('->')
    item_type = args[0]
    item_price = float(args[1])
    value = False
    if item_price > budget:
        continue

    if item_type == "Clothes":
        if item_price <= 50.00:
            value = True
    elif item_type == "Shoes":
        if item_price <= 35.00:
            value = True
    elif item_type == "Accessories":
        if item_price <= 20.50:
            value = True
    if value:
        budget -= item_price
        spent_money += item_price
        item_mark = item_price * (1 + 0.40)
        list_of_bought_items.append("%.2f" % item_mark)

for current_price in list_of_bought_items:
    sum_of_bought_items += float(current_price)
profit = sum_of_bought_items - spent_money
result = ' '.join(str(element) for element in list_of_bought_items)
print(result)
print(f'Profit: {profit :.2f}')

if sum_of_bought_items + budget >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
