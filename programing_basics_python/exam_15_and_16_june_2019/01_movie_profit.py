movie_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percent = int(input())

profit = days_count * tickets_count * ticket_price
profit -= profit * (cinema_percent / 100)

print(f"The profit from the movie {movie_name} is {profit :.2f} lv.")
