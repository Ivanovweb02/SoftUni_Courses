def collection(some_item):
    if some_item not in list_of_items:
        list_of_items.append(some_item)


def drop(some_item):
    if some_item in list_of_items:
        list_of_items.remove(some_item)


def combine_items(old_thing, new_thing):
    if old_thing in list_of_items:
        index = list_of_items.index(old_thing)
        list_of_items.insert(index + 1, new_thing)


def renew(some_item):
    if some_item in list_of_items:
        list_of_items.remove(some_item)
        list_of_items.append(some_item)


def result(some_list):
    print(', '.join(some_list))


list_of_items = input().split(', ')
instruction = input()
while instruction != 'Craft!':
    instruction = instruction.split(' - ')
    command = instruction[0]
    if command == 'Collect':
        item = instruction[1]
        collection(item)
    elif command == 'Drop':
        item = instruction[1]
        drop(item)
    elif command == 'Combine Items':
        old_item, new_item = instruction[1].split(':')
        combine_items(old_item, new_item)
    elif command == 'Renew':
        item = instruction[1]
        renew(item)

    instruction = input()

result(list_of_items)
