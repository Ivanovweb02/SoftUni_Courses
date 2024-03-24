number_of_heroes = int(input())
all_heroes = {}
for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    all_heroes[hero_name] = {}
    all_heroes[hero_name]['hp'] = int(hp)
    all_heroes[hero_name]['mp'] = int(mp)

instruction = input()
while instruction != 'End':
    instruction = instruction.split(' - ')
    command = instruction[0]
    if command == 'CastSpell':
        hero_name = instruction[1]
        mp_needed = int(instruction[2])
        spell_name = instruction[3]
        if all_heroes[hero_name]['mp'] >= mp_needed:
            all_heroes[hero_name]['mp'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == 'TakeDamage':
        hero_name = instruction[1]
        damage = int(instruction[2])
        attacker = instruction[3]
        all_heroes[hero_name]['hp'] -= damage
        if all_heroes[hero_name]['hp'] > 0:
            print(f"{hero_name} was hit for {damage} "
                  f"HP by {attacker} and now has {all_heroes[hero_name]['hp']} HP left!")
        else:
            del all_heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == 'Recharge':
        hero_name = instruction[1]
        amount = int(instruction[2])
        if (all_heroes[hero_name]['mp'] + amount) > 200:
            amount = 200 - all_heroes[hero_name]['mp']
            all_heroes[hero_name]['mp'] = 200
        else:
            all_heroes[hero_name]['mp'] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif command == 'Heal':
        hero_name = instruction[1]
        amount = int(instruction[2])
        if (all_heroes[hero_name]['hp'] + amount) > 100:
            amount = 100 - all_heroes[hero_name]['hp']
            all_heroes[hero_name]['hp'] = 100
        else:
            all_heroes[hero_name]['hp'] += amount
        print(f"{hero_name} healed for {amount} HP!")

    instruction = input()

for hero in all_heroes.keys():
    print(f"""{hero}
  HP: {all_heroes[hero]['hp']}
  MP: {all_heroes[hero]['mp']}""")
