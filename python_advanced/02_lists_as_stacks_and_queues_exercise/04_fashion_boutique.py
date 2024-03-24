clothes = list(map(int, input().split()))
rack_capacity = int(input())
sum_of_clothes = 0
rack_count = 1

while clothes:
    current_vest = clothes.pop()
    sum_of_clothes += current_vest
    if sum_of_clothes == rack_capacity and len(clothes) > 0:
        sum_of_clothes = 0
        rack_count += 1
    elif sum_of_clothes > rack_capacity:
        sum_of_clothes = 0
        sum_of_clothes += current_vest
        rack_count += 1

print(rack_count)
