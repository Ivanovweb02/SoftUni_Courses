number_of_electrons = int(input())
list_of_shells = []

for position in range(1, number_of_electrons + 1):
    if number_of_electrons == 0:
        break
    shell = 2*position**2
    if shell <= number_of_electrons:
        list_of_shells.append(shell)
        number_of_electrons -= shell
    else:
        list_of_shells.append(number_of_electrons)
        break

print(list_of_shells)
