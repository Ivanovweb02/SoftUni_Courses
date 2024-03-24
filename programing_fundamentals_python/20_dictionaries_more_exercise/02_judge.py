participators_data = {}


def participators():
    while True:
        command = input()
        if '->' not in command:
            break
        username, contest, points = command.split(' -> ')
        points = int(points)
        if contest not in participators_data.keys():
            participators_data[contest] = {username: points}

        elif username not in participators_data[contest]:
            participators_data[contest][username] = points

        elif points > participators_data[contest][username]:
            participators_data[contest][username] = points


def show_result():
    for contest, username in participators_data.items():
        print(f"{contest}: {len(participators_data[contest])} participants")
        ordered_dict = dict(sorted(username.items(), key=lambda x: (-x[1], x[0])))
        counter = 0

        for participant, points in ordered_dict.items():
            counter += 1
            print(f"{counter}. {participant} <::> {points}")
    print('Individual standings:')
    dict_with_total_points = {}
    for username in participators_data.values():
        for user, points in username.items():
            if user not in dict_with_total_points:
                dict_with_total_points[user] = 0
            dict_with_total_points[user] += points
    ordered_value = dict(sorted(dict_with_total_points.items(), key=lambda x: (-x[1], x[0])))
    counter = 0
    for name, total_points in ordered_value.items():
        counter += 1
        print(f"{counter}. {name} -> {total_points}")


participators()
show_result()
