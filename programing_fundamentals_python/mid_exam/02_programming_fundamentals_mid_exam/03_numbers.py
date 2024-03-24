list_of_number = list(map(int, input().split()))
avg_num = sum(list_of_number) / len(list_of_number)
biggest_than_avg = []

counter = 0
list_of_number = sorted(list_of_number, reverse=True)
for current_number in list_of_number:
    if current_number > avg_num and counter < 5:
        counter += 1
        biggest_than_avg.append(current_number)

if counter == 0:
    print('No')
else:
    result = ' '.join(map(str, biggest_than_avg))
    print(result)
