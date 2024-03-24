import math
import sys

count_of_easter_bread = int(input())
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
count_sugar = 0
count_flour = 0

for _ in range(1, count_of_easter_bread + 1):
    quantity_used_sugar = int(input())
    quantity_used_flour = int(input())
    count_sugar += quantity_used_sugar
    count_flour += quantity_used_flour
    if quantity_used_sugar > max_sugar:
        max_sugar = quantity_used_sugar
    if quantity_used_flour > max_flour:
        max_flour = quantity_used_flour

needed_packs_sugar = math.ceil(count_sugar / 950)
needed_packs_flour = math.ceil(count_flour / 750)

print(f"Sugar: {needed_packs_sugar}")
print(f"Flour: {needed_packs_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
