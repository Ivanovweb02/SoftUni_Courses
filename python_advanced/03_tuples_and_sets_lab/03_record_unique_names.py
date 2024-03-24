name_count = int(input())
list_of_unique_name = set()

for _ in range(name_count):
    name = input()
    list_of_unique_name.add(name)

print('\n'.join(list_of_unique_name))
