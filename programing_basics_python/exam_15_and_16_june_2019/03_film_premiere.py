projection = input()
movie_pack = input()
tickets_count = int(input())

ticket_price = 0

if projection == "John Wick":
    if movie_pack == "Drink":
        ticket_price = 12
    elif movie_pack == "Popcorn":
        ticket_price = 15
    elif movie_pack == "Menu":
        ticket_price = 19
elif projection == "Star Wars":
    if movie_pack == "Drink":
        ticket_price = 18
    elif movie_pack == "Popcorn":
        ticket_price = 25
    elif movie_pack == "Menu":
        ticket_price = 30
elif projection == "Jumanji":
    if movie_pack == "Drink":
        ticket_price = 9
    elif movie_pack == "Popcorn":
        ticket_price = 11
    elif movie_pack == "Menu":
        ticket_price = 14

total_price = ticket_price * tickets_count
if projection == "Star Wars" and tickets_count >= 4:
    total_price -= total_price * 0.30

if projection == "Jumanji" and tickets_count == 2:
    total_price -= total_price * 0.15

print(f"Your bill is {total_price :.2f} leva.")
