neighborhood = list(map(int, input().split('@')))
instruction = input()

jump = 0
while instruction != 'Love!':
    instruction = instruction.split()
    jump += int(instruction[1])
    if jump >= len(neighborhood):
        jump = 0
    hearths = neighborhood[jump]
    if hearths == 0:
        print(f"Place {jump} already had Valentine's day.")
    else:
        hearths -= 2
        neighborhood[jump] = hearths
        if hearths == 0:
            print(f"Place {jump} has Valentine's day.")

    instruction = input()

print(f"Cupid's last position was {jump}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    counter = 0
    for house in neighborhood:
        if house != 0:
            counter += 1
    print(f"Cupid has failed {counter} places.")
