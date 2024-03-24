from collections import deque

materials = [int(material) for material in input().split()]
magic_level = deque([int(magic) for magic in input().split()])

crafted = []
presents = {
     150: 'Doll',
     250: 'Wooden train',
     300: 'Teddy bear',
     400: 'Bicycle'
}


while materials and magic_level:
    curr_material = materials.pop() if magic_level[0] or not materials[-1] else 0
    curr_magic = magic_level.popleft() if curr_material or not magic_level[0] else 0

    if not curr_magic:
        continue

    product = curr_material * curr_magic

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(curr_material + curr_magic)
    elif product > 0:
        materials.append(curr_material + 15)

if {'Doll', 'Wooden train'}.issubset(crafted) or {'Teddy bear', 'Bicycle'}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
