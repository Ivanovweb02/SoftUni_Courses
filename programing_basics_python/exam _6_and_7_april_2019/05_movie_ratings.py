import sys

count_of_movies = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
total_rating = 0

for current_movie in range(1, count_of_movies + 1):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_rating_movie = movie_name
    elif movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rating_movie = movie_name

avg_rating = total_rating / count_of_movies
print(f"{highest_rating_movie} is with highest rating: {highest_rating :.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating :.1f}")
print(f"Average rating: {avg_rating :.1f}")
