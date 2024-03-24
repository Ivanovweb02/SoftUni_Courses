number = int(input())
p_1 = 0
p_2 = 0
p_3 = 0

for _ in range(1, number + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        p_1 += 1
    if current_number % 3 == 0:
        p_2 += 1
    if current_number % 4 == 0:
        p_3 += 1

percent_p_1 = (p_1 / number) * 100
percent_p_2 = (p_2 / number) * 100
percent_p_3 = (p_3 / number) * 100
print(f"{percent_p_1 :.2f}%")
print(f"{percent_p_2 :.2f}%")
print(f"{percent_p_3 :.2f}%")
