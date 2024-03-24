import re

list_of_participant = input().split(', ')
info = input()
participants_info = {}
name_pattern = r'([A-Za-z])'
distance_pattern = r'([0-9])'

while info != 'end of race':
    name = ''
    distance = 0
    for char in info:
        name_matches = re.finditer(name_pattern, char)
        distance_matches = re.finditer(distance_pattern, char)
        for match in name_matches:
            name += match.group()
        for match in distance_matches:
            distance += int(match.group())
    if name in list_of_participant:
        if name not in participants_info:
            participants_info[name] = 0
        participants_info[name] += distance

    info = input()


ordered_dict = sorted(participants_info.items(), key=lambda item: (-item[1]))
print(f"""1st place: {(ordered_dict[0])[0]}
2nd place: {(ordered_dict[1])[0]}
3rd place: {(ordered_dict[2])[0]}
""")
