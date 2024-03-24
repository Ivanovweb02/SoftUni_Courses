command = input()

movie_count = 0
best_movie = ""
winner_point = 0

is_limit_reached = False

while command != "STOP":
    movie_name = command
    movie_count += 1
    if movie_count == 7:
        is_limit_reached = True
        break
    current_point = 0
    movie_point = 0
    for char in movie_name:
        ascii_value = ord(char)

        if "a" <= char <= "z":
            current_point = ascii_value - (2 * len(movie_name))
            movie_point += current_point
        elif "A" <= char <= "Z":
            current_point = ascii_value - len(movie_name)
            movie_point += current_point
        else:
            current_point = ascii_value
            movie_point += current_point

        if movie_point > winner_point:
            winner_point = movie_point
            best_movie = movie_name

    command = input()

if is_limit_reached:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {winner_point} ASCII sum.")
