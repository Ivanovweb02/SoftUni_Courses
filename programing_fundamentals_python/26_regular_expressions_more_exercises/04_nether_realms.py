import re

demons_name = re.split(', *', input())
print(demons_name)
exit()
demons_book = {}
demon_health_pattern = r'[^\d\+\-*\/\.]'
demon_damage_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
demons_operator_pattern = r'[*\/]'

for name in demons_name:
    demon_name = name.strip()
    demon_health = re.findall(demon_health_pattern, demon_name)
    demons_book[demon_name] = []
    demons_book[demon_name].append(sum(ord(match) for match in demon_health))

    demon_damage = re.finditer(demon_damage_pattern, demon_name)
    operations = re.findall(demons_operator_pattern, demon_name)
    current_damage = 0

    for value in demon_damage:
        current_damage += float(value.group(0))

    for operation in operations:
        if operation == '*':
            current_damage *= 2
        elif operation == '/':
            current_damage /= 2

    demons_book[demon_name].append(current_damage)

for demon, quality in sorted(demons_book.items()):
    print(f"{demon} - {quality[0]} health, {quality[1] :.2f} damage")
