energy = 100
coin = 100
list_of_events = input().split('|')
are_events_managed = True
for event in list_of_events:
    args = event.split('-')
    event_or_ingredient = args[0]
    number = int(args[1])

    if event_or_ingredient == 'rest':
        current_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_or_ingredient == 'order':
        if energy >= 30:
            coin += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coin >= number:
            coin -= number
            print(f"You bought {event_or_ingredient}.")
        else:
            are_events_managed = False
            break

if are_events_managed:
    print("Day completed!")
    print(f"Coins: {coin}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {event_or_ingredient}.")
