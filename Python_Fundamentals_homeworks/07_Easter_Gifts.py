list_of_gifts = input().split()
command = input()

while command != "No Money":
    gift_command = command.split()
    if 'OutOfStock' in gift_command:
        element = gift_command[1]
        for current_index in range(len(list_of_gifts)):
            if list_of_gifts[current_index] == element:
                list_of_gifts[current_index] = 'None'
    elif 'Required' in gift_command:
        if len(list_of_gifts) > int(gift_command[2]) > 0:
            index = int(gift_command[2])
            list_of_gifts[index] = gift_command[1]
    elif 'JustInCase' in gift_command:
        list_of_gifts[-1] = gift_command[1]
    command = input()

while 'None' in list_of_gifts:
    list_of_gifts.remove('None')

result = ' '.join(str(gift) for gift in list_of_gifts)
print(result)
