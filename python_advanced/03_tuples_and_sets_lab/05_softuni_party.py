count = int(input())

reservation_list = set()
for _ in range(count):
    reservation_num = input()
    reservation_list.add(reservation_num)

guest = input()
while guest != 'END':
    if guest in reservation_list:
        reservation_list.remove(guest)
    guest = input()

print(len(reservation_list))
result = sorted(reservation_list)
print('\n'.join(result))
