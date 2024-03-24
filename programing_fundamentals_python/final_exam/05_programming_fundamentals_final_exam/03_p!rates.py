command = input()
targeted_cities = {}

while command != 'Sail':
    city, population, gold = command.split('||')

    if city not in targeted_cities.keys():
        targeted_cities[city] = {}
        targeted_cities[city]['population'] = int(population)
        targeted_cities[city]['gold'] = int(gold)
    else:
        targeted_cities[city]['population'] += int(population)
        targeted_cities[city]['gold'] += int(gold)

    command = input()

instruction = input()

while instruction != 'End':
    instruction = instruction.split('=>')
    event = instruction[0]
    if event == 'Plunder':
        town = instruction[1]
        people = int(instruction[2])
        gold = int(instruction[3])
        targeted_cities[town]['population'] -= people
        targeted_cities[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if targeted_cities[town]['population'] == 0 or targeted_cities[town]['gold'] == 0:
            del targeted_cities[town]
            print(f"{town} has been wiped off the map!")

    elif event == 'Prosper':
        town = instruction[1]
        gold = int(instruction[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targeted_cities[town]['gold']} gold.")

    instruction = input()

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities.keys())} wealthy settlements to go to:")
    for city in targeted_cities.keys():
        print(f"{city} -> Population: {targeted_cities[city]['population']} citizens, Gold: {targeted_cities[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
