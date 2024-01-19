animals = input().split(', ')

if animals[-1] == 'wolf':
    print("Please go away and stop eating my sheep")

else:
    index = animals.index('wolf')
    sheep_location = len(animals) - (index + 1)
    print(f"Oi! Sheep number {sheep_location}! You are about to be eaten by a wolf!")
