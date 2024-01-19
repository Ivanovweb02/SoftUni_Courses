def sequence(some_num: int) -> list:
    some_list = []
    current_num = 1
    for _ in range(some_num):
        counter = 0
        for index in range(len(some_list) - 1, -1, -1):
            counter += 1
            current_num += some_list[index]
            if counter == 3:
                break
        some_list.append(current_num)
        current_num = 0
    return some_list


count = int(input())

print(*sequence(count), sep=' ')
