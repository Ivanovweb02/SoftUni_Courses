import time

sequence_of_nums = list(map(int, input().split()))
result = int(input())
numbers = []

start = time.time()
index = 0
while index != len(sequence_of_nums) - 1:
    for curr_index in range(0, len(sequence_of_nums) - 1):
        num_1 = sequence_of_nums[index]
        num_2 = sequence_of_nums[curr_index + 1]
        if num_1 + num_2 == result:
            if num_1 not in numbers and num_2 not in numbers:
                numbers.append(num_1)
                numbers.append(num_2)
                break
    index += 1

for index in range(0, len(numbers), 2):
    num_1 = numbers[index]
    num_2 = numbers[index + 1]
    print(f"{num_1} + {num_2} = {result}")

end = time.time()
print(end-start)
