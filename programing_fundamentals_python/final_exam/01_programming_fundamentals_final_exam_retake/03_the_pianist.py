number_of_pieces = int(input())
collection = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    collection[piece] = {}
    collection[piece]['composer'] = composer
    collection[piece]['key'] = key

instruction = input()
while instruction != 'Stop':
    instruction = instruction.split('|')
    command = instruction[0]
    if command == 'Add':
        piece = instruction[1]
        composer = instruction[2]
        key = instruction[3]
        if piece not in collection.keys():
            collection[piece] = {}
            collection[piece]['composer'] = composer
            collection[piece]['key'] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command == 'Remove':
        piece = instruction[1]
        if piece in collection.keys():
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == 'ChangeKey':
        piece = instruction[1]
        new_key = instruction[2]
        if piece in collection.keys():
            collection[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    instruction = input()

for piece in collection.keys():
    print(f"{piece} -> Composer: {collection[piece]['composer']}, Key: {collection[piece]['key']}")
