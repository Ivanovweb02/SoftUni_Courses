final_sector = input()
row_in_first_sector = int(input())
seats_in_odd_row = int(input())
total_seats = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for sector in range(ord('A'), ord(final_sector) + 1):
    if chr(sector) != 'A':
        row_in_first_sector += 1

    for row in range(1, row_in_first_sector + 1):
        if row % 2 == 0:
            seats_in_even_row = 2 + seats_in_odd_row
            for seats in range(seats_in_even_row):
                total_seats += 1
                print(f'{chr(sector)}{row}{alphabet[seats]}')
        else:
            for seats in range(seats_in_odd_row):
                total_seats += 1
                print(f'{chr(sector)}{row}{alphabet[seats]}')
print(total_seats)
