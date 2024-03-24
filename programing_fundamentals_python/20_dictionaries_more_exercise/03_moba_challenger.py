instruction = input()
player_info = {}
best_players = []


def adding_players(player, position, skill):
    if player not in player_info.keys():
        player_info[player] = {position: skill}
    elif position not in player_info[player]:
        player_info[player][position] = skill
    elif skill > player_info[player][position]:
        player_info[player][position] = skill


def duel_players(player_1, player_2):
    if (player_1 and player_2) in player_info.keys():
        for current_position in player_info[player_1]:
            if current_position in player_info[player_2]:
                total_points_player_1 = sum(player_info[player_1].values())
                total_points_player_2 = sum(player_info[player_2].values())
                if total_points_player_1 > total_points_player_2:
                    del player_info[player_2]
                elif total_points_player_2 > total_points_player_1:
                    del player_info[player_1]
                break


while instruction != 'Season end':
    if '->' in instruction:
        instruction = instruction.split(' -> ')
        adding_players(instruction[0], instruction[1], int(instruction[2]))
    elif 'vs' in instruction:
        instruction = instruction.split(' vs ')
        duel_players(instruction[0], instruction[1])
    instruction = input()


def showing_data():
    for current_name in player_info:
        best_players.append({'name': current_name, 'total_score': sum(player_info[current_name].values())})
    for output in sorted(best_players, key=lambda item: (-item['total_score'], item['name'])):
        print(f"{output['name']}: {output['total_score']} skill")
        for position, skill in sorted(player_info[output['name']].items(), key=lambda item: (-item[1], item[0])):
            print(f"- {position} <::> {skill}")


showing_data()
