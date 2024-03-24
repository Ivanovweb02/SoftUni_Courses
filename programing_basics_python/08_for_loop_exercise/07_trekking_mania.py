count_of_group = int(input())
musala_count = 0
montblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(count_of_group):
    number_of_people = int(input())

    if number_of_people < 6:
        musala_count += number_of_people

    elif number_of_people < 13:
        montblan_count += number_of_people
    elif number_of_people < 26:
        kilimanjaro_count += number_of_people
    elif number_of_people < 41:
        k2_count += number_of_people
    else:
        everest_count += number_of_people

total_people = musala_count \
               + montblan_count \
               + kilimanjaro_count \
               + k2_count \
               + everest_count

percent_musala = musala_count / total_people * 100
percent_montblan = montblan_count / total_people * 100
percent_kilimanjaro = kilimanjaro_count / total_people * 100
percent_k2 = k2_count / total_people * 100
percent_everest = everest_count / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
