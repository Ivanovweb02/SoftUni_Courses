def list_of_do_to():
    to_do_list = []
    while True:
        note = input()
        if note == 'End':
            break

        to_do_list.append(note)
    sorted_list = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
    return [element.split('-')[1] for element in sorted_list]


result = list_of_do_to()
print(result)
