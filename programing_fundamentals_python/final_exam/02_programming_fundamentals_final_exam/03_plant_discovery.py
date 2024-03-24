number_of_lines = int(input())
plant_dict = {}

for _ in range(number_of_lines):
    plant, rarity = input().split('<->')
    if plant not in plant_dict.keys():
        plant_dict[plant] = {}
        plant_dict[plant]['rarity'] = rarity
        plant_dict[plant]['rating'] = []
    plant_dict[plant]['rarity'] = rarity
instruction = input()

while instruction != 'Exhibition':
    instruction = instruction.split(': ')
    command = instruction[0]
    if command == 'Rate':
        plant, rating = instruction[1].split(' - ')
        if plant in plant_dict.keys():
            plant_dict[plant]['rating'].append(int(rating))
        else:
            print('error')
    elif command == 'Update':
        plant, new_rarity = instruction[1].split(' - ')
        if plant in plant_dict.keys():
            plant_dict[plant]['rarity'] = new_rarity
        else:
            print('error')
    elif command == 'Reset':
        plant = instruction[1]
        if plant in plant_dict.keys():
            plant_dict[plant]['rating'].clear()
        else:
            print('error')

    instruction = input()
print("Plants for the exhibition:")
for plant in plant_dict.keys():
    if plant_dict[plant]['rating']:
        avg_rating = sum(plant_dict[plant]['rating']) / len(plant_dict[plant]['rating'])
    else:
        avg_rating = 0
    print(f"- {plant}; Rarity: {plant_dict[plant]['rarity']}; Rating: {avg_rating :.2f}")
