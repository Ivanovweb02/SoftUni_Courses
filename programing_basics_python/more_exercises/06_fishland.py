mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kilograms = float(input())
safrid_kilograms = float(input())
mussels_kilograms = int(input())

# •	Паламуд – 60% по-скъп от скумрията
# •	Сафрид – 80% по-скъп от цацата
# •	Миди – 7.50 лв. за килограм

bonito_price = mackerel_price * (1 + 0.60)
safrid_price = sprinkle_price * (1 + 0.80)
mussels_price = 7.50 * float(mussels_kilograms)

total_price = bonito_price * bonito_kilograms \
              + safrid_price * safrid_kilograms \
              + mussels_price
print(f"{total_price:.2f}")
