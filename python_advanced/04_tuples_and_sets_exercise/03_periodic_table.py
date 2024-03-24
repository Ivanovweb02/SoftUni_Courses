count = int(input())
periodic_table = set()

for _ in range(count):
    chemical_elements = input().split()
    for element in chemical_elements:
        periodic_table.add(element)

print('\n'.join(periodic_table))
