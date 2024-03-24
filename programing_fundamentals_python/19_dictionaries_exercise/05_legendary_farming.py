material_list = input().lower().split()
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junks = {}

is_material_found = False
while True:
    for index in range(0, len(material_list), 2):
        material = material_list[index + 1]
        quantity = int(material_list[index])
        if material in key_materials:
            key_materials[material] += quantity
            if material == 'shards':
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    print("Shadowmourne obtained!")
                    is_material_found = True
                    break
            elif material == 'fragments':
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    print("Valanyr obtained!")
                    is_material_found = True
                    break
            elif material == 'motes':
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    print("Dragonwrath obtained!")
                    is_material_found = True
                    break
        else:
            if material not in junks:
                junks[material] = 0
            junks[material] += quantity

    if is_material_found:
        break
    material_list = input().lower().split()

# ordered_key_material = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
# ordered_junk = sorted(junks.items(), key=lambda x: x[0])

for (material, quantity) in key_materials.items():
    print(f"{material}: {quantity}")
for (material, quantity) in junks.items():
    print(f"{material}: {quantity}")
