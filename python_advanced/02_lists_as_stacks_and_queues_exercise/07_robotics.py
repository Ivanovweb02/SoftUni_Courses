from collections import deque


def starting_time():
    hour, minutes, seconds = list(map(int, input().split(':')))
    return hour, minutes, seconds


def adding_info(times, busyness):
    for statistic in robots_stats:
        robot = statistic[0]
        time = int(statistic[1])
        if robot not in times.keys():
            times[robot] = time
            busyness[robot] = time


def putting_products():
    command = input()
    while command != 'End':
        product = command
        queue_of_products.append(product)
        command = input()


def time_checking(hour, minutes, seconds):
    if seconds >= 60:
        seconds -= 60
        minutes += 1
    if minutes >= 60:
        minutes -= 60
        hour += 1
    if hour >= 24:
        hour -= 24
    return hour, minutes, seconds


def robots_management():
    hour, minutes, seconds = starting_time()
    adding_info(processing_times, robots_busyness)
    putting_products()
    while queue_of_products:
        seconds += 1
        current_product = queue_of_products.popleft()
        hour, minutes, seconds = time_checking(hour, minutes, seconds)

        is_product_taken = False
        for robot_name in robots_busyness.keys():
            if robots_busyness[robot_name] == processing_times[robot_name]:
                if not is_product_taken:
                    robots_busyness[robot_name] -= processing_times[robot_name]
                    print(f"{robot_name} - {current_product} [{hour:02d}:{minutes:02d}:{seconds:02d}]")
                    is_product_taken = True

        for robot_name in robots_busyness.keys():
            if robots_busyness[robot_name] < processing_times[robot_name]:
                robots_busyness[robot_name] += 1
        if not is_product_taken:
            queue_of_products.append(current_product)


robots_stats = input().split(';')
robots_stats = [statistic .split('-') for statistic in robots_stats]
processing_times = {}
robots_busyness = {}
queue_of_products = deque()

robots_management()
