count = int(input())
longest_intersection = set()

for _ in range(count):
    first_length, second_length = input().split('-')
    first_collection = set()
    second_collection = set()
    start_1, end_1 = list(map(int, first_length.split(',')))
    start_2, end_2 = list(map(int, second_length.split(',')))
    for num_1 in range(start_1, end_1 + 1):
        first_collection.add(num_1)
    for num_2 in range(start_2, end_2 + 1):
        second_collection.add(num_2)
    intersection = first_collection & second_collection
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

result = [str(num) for num in longest_intersection]
print(f"Longest intersection is [{', '.join(result)}] with length {len(longest_intersection)}")
