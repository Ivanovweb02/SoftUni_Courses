health = 100
bitcoin = 0
dangerous_room = input().split('|')

is_survived = True
for index in range(len(dangerous_room)):
    current_room = dangerous_room[index].split()
    command = current_room[0]
    number = int(current_room[1])
    if command == 'potion':
        health_amount = number
        health += health_amount
        if health > 100:
            diff = abs((health - 100) - number)
            health = 100
            health_amount = diff
        print(f"You healed for {health_amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        monster = command
        damage = number
        health -= damage
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {index + 1}")
            is_survived = False
            break
        else:
            print(f"You slayed {monster}.")

if is_survived:
    print(f"""You've made it!
Bitcoins: {bitcoin}
Health: {health}""")
