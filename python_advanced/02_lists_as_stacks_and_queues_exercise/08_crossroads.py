from collections import deque

green_light = int(input())
green_light_duration = green_light
free_window_duration = int(input())
command = input()
traffic_queue = deque()
hit_car = ''
hit_point = ''
passed_car = 0

is_crash = False
while command != 'END':
    if command == 'green':
        green_light = green_light_duration
        for _ in range(len(traffic_queue)):
            if green_light > 0:
                car = traffic_queue.popleft()
                if len(car) > green_light:
                    green_light += free_window_duration
                    if len(car) > green_light:
                        is_crash = True
                        hit_car = car
                        hit_point = car[green_light]
                        break
                    else:
                        passed_car += 1
                        break
                else:
                    green_light -= len(car)
                    passed_car += 1
    else:
        traffic_queue.append(command)
    if is_crash:
        break
    command = input()


if is_crash:
    print(f"""A crash happened!
{hit_car} was hit at {hit_point}.""")
else:
    print(f"""Everyone is safe.
{passed_car} total cars passed the crossroads.""")
