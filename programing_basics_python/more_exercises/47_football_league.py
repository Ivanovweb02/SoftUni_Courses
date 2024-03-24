stadium_capacity = int(input())
total_fans = int(input())
sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for fan in range(total_fans):
    sector = input()
    if sector == "A":
        sector_a_fans += 1
    elif sector == "B":
        sector_b_fans += 1
    elif sector == "V":
        sector_v_fans += 1
    elif sector == "G":
        sector_g_fans += 1

percent_of_sector_a = sector_a_fans / total_fans * 100
percent_of_sector_b = sector_b_fans / total_fans * 100
percent_of_sector_v = sector_v_fans / total_fans * 100
percent_of_sector_g = sector_g_fans / total_fans * 100
percent_of_total_fans = total_fans / stadium_capacity * 100
print(f"{percent_of_sector_a :.2f}%")
print(f"{percent_of_sector_b :.2f}%")
print(f"{percent_of_sector_v :.2f}%")
print(f"{percent_of_sector_g :.2f}%")
print(f"{percent_of_total_fans :.2f}%")
