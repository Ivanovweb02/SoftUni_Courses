number = int(input())
p2 = 0
p3 = 0
p4 = 0

for _ in range(1, number + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        p2 += 1
    if current_number % 3 == 0:
        p3 += 1
    if current_number % 4 == 0:
        p4 += 1

p2_percent = p2 / number * 100
p3_percent = p3 / number * 100
p4_percent = p4 / number * 100

print(f"{p2_percent :.2f}%")
print(f"{p3_percent :.2f}%")
print(f"{p4_percent :.2f}%")
