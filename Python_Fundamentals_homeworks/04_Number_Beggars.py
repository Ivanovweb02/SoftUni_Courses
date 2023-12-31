money = input().split(', ')
count_of_beggars = int(input())
beggars_sum = []
index = 0
for current_beggars in range(1, count_of_beggars + 1):
    current_beggars_sum = 0
    for current_index in range(index, len(money), count_of_beggars):
        current_beggars_sum += int(money[current_index])

    beggars_sum.append(current_beggars_sum)
    index += 1
print(beggars_sum)
