def sorted_list_of_names():
    name_in_list = [name for name in input().split(', ')]
    return sorted(name_in_list, key=lambda x: (-len(x), x))


print(sorted_list_of_names())
