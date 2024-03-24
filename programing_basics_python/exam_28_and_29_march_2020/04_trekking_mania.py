group_count = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k_2 = 0
everest = 0

for _ in range(group_count):
    people_in_group = int(input())

    if people_in_group < 6:
        musala += people_in_group
    elif people_in_group < 13:
        mont_blanc += people_in_group
    elif people_in_group < 26:
        kilimanjaro += people_in_group
    elif people_in_group < 41:
        k_2 += people_in_group
    else:
        everest += people_in_group

total_climbers = musala \
                 + mont_blanc \
                 + kilimanjaro \
                 + k_2 \
                 + everest

percent_musala = musala / total_climbers * 100
percent_mont_blanc = mont_blanc / total_climbers * 100
percent_kilimanjaro = kilimanjaro / total_climbers * 100
percent_k_2 = k_2 / total_climbers * 100
percent_everest = everest / total_climbers * 100

print(f"{percent_musala :.2f}%")
print(f"{percent_mont_blanc :.2f}%")
print(f"{percent_kilimanjaro :.2f}%")
print(f"{percent_k_2 :.2f}%")
print(f"{percent_everest :.2f}%")
