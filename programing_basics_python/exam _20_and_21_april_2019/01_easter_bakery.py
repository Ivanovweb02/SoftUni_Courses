flour_price_per_kilogram = float(input())
kilogram_flour = float(input())
kilogram_sugar = float(input())
count_eggs = int(input())
packets_of_yeast = int(input())

price_per_kilogram_sugar = flour_price_per_kilogram * (1 - 0.25)
price_per_egg_pack = flour_price_per_kilogram * (1 + 0.10)
price_packets_of_yeast = price_per_kilogram_sugar * (1 - 0.80)

total_price = flour_price_per_kilogram * kilogram_flour \
              + price_per_kilogram_sugar * kilogram_sugar \
              + price_per_egg_pack * count_eggs \
              + price_packets_of_yeast * packets_of_yeast

print(f"{total_price :.2f}")
