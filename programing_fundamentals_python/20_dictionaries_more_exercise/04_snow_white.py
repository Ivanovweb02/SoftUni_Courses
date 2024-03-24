dwarf_info = {}
result = []
hat_len = 'hat len'
name_d = 'name'
physic_d = 'physic'
hat_d = 'hat'
command = input()


def adding_info(name, hat_color, physics):
    if hat_color not in dwarf_info.keys():
        dwarf_info[hat_color] = {name: physics}
    elif name not in dwarf_info[hat_color]:
        dwarf_info[hat_color][name] = physics
    elif physics > dwarf_info[hat_color][name]:
        dwarf_info[hat_color][name] = physics


while command != 'Once upon a time':
    command = command.split(' <:> ')
    adding_info(command[0], command[1], int(command[2]))
    command = input()


def showing_info():
    for hat in dwarf_info:
        for name, physics in dwarf_info[hat].items():
            result.append({hat_len: len(dwarf_info[hat]), name_d: name, physic_d: physics, hat_d: hat})
    for output in sorted(result, key=lambda item: (-item[physic_d], -item[hat_len])):
        print(f"({output[hat_d]}) {output[name_d]} <-> {output[physic_d]}")


showing_info()
