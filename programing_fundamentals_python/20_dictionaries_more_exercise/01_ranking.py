contest_data = {}
participators_data = {}


def contests():
    while True:
        command = input()
        if ':' not in command:
            break

        contest, password = command.split(':')
        contest_data[contest] = password


def submissions():
    while True:
        command = input()
        if '=>' not in command:
            break
        contest, password, username, points = command.split('=>')
        points = int(points)

        if contest not in contest_data.keys():
            continue
        if password != contest_data[contest]:
            continue
        if username not in participators_data:
            participators_data[username] = {contest: points}

        elif contest not in participators_data[username]:
            participators_data[username][contest] = points

        elif contest in participators_data[username]:
            if points > participators_data[username][contest]:
                participators_data[username][contest] = points


def best_score():
    list_values = {}
    for name, value in participators_data.items():
        list_values[name] = sum(value.values())
    best_candidate = max(list_values, key=list_values.get)
    total_score = max(list_values.values())
    print(f"Best candidate is {best_candidate} with total {total_score} points.")


def show_ranking_result():
    ordered_dictionary = dict(sorted(participators_data.items()))
    print('Ranking:')
    for username, contest in ordered_dictionary.items():
        print(username)
        value_dict = dict(sorted(contest.items(), key=lambda item: -item[1]))
        for key, value in value_dict.items():
            print('# ', key, '->', value)


contests()
submissions()
best_score()
show_ranking_result()
