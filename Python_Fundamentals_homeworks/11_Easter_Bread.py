budget = float(input())
price_per_kilogram_flour = float(input())
price_per_pack_of_eggs = 0.75 * price_per_kilogram_flour
price_per_litre_milk = price_per_kilogram_flour * (1 + 0.25)
count_of_loaves = 0
count_of_colored_eggs = 0

while True:
    total_cost_per_loaf = price_per_pack_of_eggs \
                          + price_per_kilogram_flour \
                          + (price_per_litre_milk / 4)
    if budget > total_cost_per_loaf:
        budget -= total_cost_per_loaf
        count_of_loaves += 1
        count_of_colored_eggs += 3
    else:
        break
    if count_of_loaves % 3 == 0:
        count_of_colored_eggs -= count_of_loaves - 2

print(f"You made {count_of_loaves} loaves of Easter bread! Now you have "
      f"{count_of_colored_eggs} eggs and {budget :.2f}BGN left.")
