hour = int(input())
minutes = int(input())

minutes += 15
if minutes > 59:
    hour += 1
    minutes -= 60

if hour > 23:
    hour -= 24
print(f'{hour}:{minutes :02d}')
