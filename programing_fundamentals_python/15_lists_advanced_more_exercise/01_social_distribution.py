import sys

population = list(map(int, input().split(', ')))
minimum_wealth = int(input())
max_wealth = 0
is_equal_possible = True

for digit in range(len(population)):
    if population[digit] < minimum_wealth:
        max_wealth = max(population)
        diff = minimum_wealth - population[digit]
        if (max(population) - diff) >= minimum_wealth:
            population[digit] += diff
            index = population.index(max_wealth)
            population[index] = max_wealth - diff

        else:
            print("No equal distribution possible")
            is_equal_possible = False
            break

if is_equal_possible:
    print(population)
