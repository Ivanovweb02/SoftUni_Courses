current_energy = int(input())
command = input()
win_battle = 0

is_energy_run_out = False
while command != 'End of battle':
    enemy_distance = int(command)
    if current_energy >= enemy_distance:
        win_battle += 1
        current_energy -= enemy_distance
    else:
        is_energy_run_out = True
        break
    if win_battle % 3 == 0:
        current_energy += win_battle

    command = input()

if is_energy_run_out:
    print(f"Not enough energy! Game ends with {win_battle} won battles and {current_energy} energy")
else:
    print(f"Won battles: {win_battle}. Energy left: {current_energy}")
