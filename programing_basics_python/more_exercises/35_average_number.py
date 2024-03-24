number = int(input())
total_sum = 0

for _ in range(1, number + 1):
    current_number = int(input())
    total_sum += current_number

avr_number = total_sum / number
print(f"{avr_number :.2f}")
