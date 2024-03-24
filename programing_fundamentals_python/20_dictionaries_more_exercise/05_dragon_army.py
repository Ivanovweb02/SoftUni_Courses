number_of_dragons = int(input())
dragons_data = {}


def adding_info(curr_type, curr_name, curr_damage, curr_health, curr_armor):
    dragons_data[curr_type] = dragons_data.get(dragon_type, dict())
    dragons_data[curr_type][curr_name] = dragons_data.get(name, dict())
    dragons_data[curr_type][curr_name]['damage'] = curr_damage
    dragons_data[curr_type][curr_name]['health'] = curr_health
    dragons_data[curr_type][curr_name]['armor'] = curr_armor


def show_result():
    for color in dragons_data.keys():
        dragon_damage, dragon_health, dragon_armor = 0, 0, 0
        for dragon_name in dragons_data[color]:
            dragon_damage += dragons_data[color][dragon_name]['damage']
            dragon_health += dragons_data[color][dragon_name]['health']
            dragon_armor += dragons_data[color][dragon_name]['armor']
        total_dragons = len(dragons_data[color])
        print(f"{color}::({(dragon_damage / total_dragons) :.2f}/"
              f"{(dragon_health / total_dragons) :.2f}/{(dragon_armor / total_dragons) :.2f})")
        for dragon_name in sorted(dragons_data[color].keys()):
            curr_damage = dragons_data[color][dragon_name]['damage']
            curr_health = dragons_data[color][dragon_name]['health']
            curr_armor = dragons_data[color][dragon_name]['armor']
            print(f"-{dragon_name} -> damage: {curr_damage}, health: {curr_health}, armor: {curr_armor}")


for _ in range(number_of_dragons):
    dragon_info = input().split()
    dragon_type = dragon_info[0]
    name = dragon_info[1]
    damage = 45
    health = 250
    armor = 10
    if dragon_info[2] != 'null':
        damage = int(dragon_info[2])
    if dragon_info[3] != 'null':
        health = int(dragon_info[3])
    if dragon_info[4] != 'null':
        armor = int(dragon_info[4])
    adding_info(dragon_type, name, damage, health, armor)

show_result()
