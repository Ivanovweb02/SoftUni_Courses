# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.

CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

# •	Брой пилешки менюта – цяло число в интервала [0 … 99]
# •	Брой менюта с риба – цяло число в интервала [0 … 99]
# •	Брой вегетариански менюта – цяло число в интервала [0 … 99]

number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegetarian_menu = int(input())

total_sum = (CHICKEN_MENU_PRICE * number_of_chicken_menu) \
            + (FISH_MENU_PRICE * number_of_fish_menu) \
            + (VEGETARIAN_MENU_PRICE * number_of_vegetarian_menu)

dessert = 0.20 * total_sum

final_sum = total_sum + dessert + DELIVERY_PRICE

print(final_sum)
