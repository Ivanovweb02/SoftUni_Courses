first_player_name = input()
second_player_name = input()
command = input()
first_player_point = 0
second_player_point = 0
winner = ""
winner_points = 0
is_number_wars = False

while command != "End of game":
    card_from_first_player = int(command)
    card_from_second_player = int(input())
    if card_from_first_player > card_from_second_player:
        first_player_point += card_from_first_player - card_from_second_player
    elif card_from_second_player > card_from_first_player:
        second_player_point += card_from_second_player - card_from_first_player
    else:
        is_number_wars = True
        final_card_from_first_player = int(input())
        final_card_from_second_player = int(input())
        if final_card_from_first_player > final_card_from_second_player:
            winner = first_player_name
            winner_points = first_player_point

        elif final_card_from_second_player > final_card_from_first_player:
            winner = second_player_name
            winner_points = second_player_point
        break
    command = input()

if is_number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winner_points} points")

else:
    print(f"{first_player_name} has {first_player_point} points")
    print(f"{second_player_name} has {second_player_point} points")
