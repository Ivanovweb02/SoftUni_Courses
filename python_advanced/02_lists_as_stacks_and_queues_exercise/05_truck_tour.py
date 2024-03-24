from collections import deque

count_of_petrol_pumps = int(input())
queue = deque()

for _ in range(count_of_petrol_pumps):
    data = list(map(int, input().split()))
    queue.append(data)

quantity_of_petrol = 0
index = 0
start_point = 0

while index != len(queue) - 1:
    current_data = queue[index]
    amount_of_petrol = current_data[0]
    distance = current_data[1]
    quantity_of_petrol += amount_of_petrol
    if quantity_of_petrol >= distance:
        quantity_of_petrol -= distance
        index += 1
    else:
        index = 0
        quantity_of_petrol = 0
        queue.rotate(-1)
        start_point += 1

print(start_point)
