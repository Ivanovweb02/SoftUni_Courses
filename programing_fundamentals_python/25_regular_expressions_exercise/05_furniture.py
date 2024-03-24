import re

list_of_furniture = []
total_cost = 0
command = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        total_cost += float(price) * int(quantity)
        list_of_furniture.append(furniture)
    command = input()

print('Bought furniture:')
for furniture in list_of_furniture:
    print(furniture)
print(f"Total money spend: {total_cost :.2f}")
