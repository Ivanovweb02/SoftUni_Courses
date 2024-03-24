import re

count_of_lines = int(input())
planets_info = {'Attacked': [], 'Destroyed': [], 'A': 'Attacked', 'D': 'Destroyed'}
pattern = re.compile(r'@(?P<planet_name>[A-Za-z]+)([^\@\-\!\:\>]*)'
                     r':(?P<population>[0-9]+)([^\@\-\!\:\>]*)'
                     r'!(?P<attack_type>[AD])!([^\@\-\!\:\>]*)'
                     r'->(?P<soldier_count>[0-9]+)')

for text in range(count_of_lines):
    current_text = input()
    decrypt_code = sum(current_text.lower().count(char) for char in 'star')
    decrypted_text = ''.join(chr(ord(char) - decrypt_code) for char in current_text)
    result = re.finditer(pattern, decrypted_text)
    for output in result:
        planets_info[planets_info[output['attack_type']]].append(output['planet_name'])

for type_attack in list(planets_info.keys())[:2]:
    planet_count = len(planets_info[type_attack])
    print(f"{type_attack} planets: {planet_count}")
    if planet_count:
        for planet in sorted(planets_info[type_attack]):
            print(f"-> {planet}")
