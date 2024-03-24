import re

key = list(map(int, input().split()))
command = input()
type_pattern = r'&([A-Za-z]+)&'
coordinates_pattern = r'<([A-Za-z0-9]+)>'
while command != 'find':
    index_key = 0
    treasure_data = ''
    for index_char in range(len(command)):
        if index_key >= len(key):
            index_key = 0
        ascii_value = ord(command[index_char])
        ascii_value -= key[index_key]
        treasure_data += chr(ascii_value)
        index_key += 1
    type_match = re.search(type_pattern, treasure_data)
    coordinates_match = re.search(coordinates_pattern, treasure_data)
    treasure_type = type_match.group(1)
    coordinates = coordinates_match.group(1)

    print(f"Found {treasure_type} at {coordinates}")
    command = input()
