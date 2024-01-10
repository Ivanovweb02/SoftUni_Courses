list_of_numbers = list(map(int, input().split(', ')))

filtered_num = map(
    lambda x: x if list_of_numbers[x] % 2 == 0 else 'no',
    range(len(list_of_numbers))
)
even_indices = list(filter(lambda a: a != 'no', filtered_num))
print(even_indices)
