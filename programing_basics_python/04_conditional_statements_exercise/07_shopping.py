petur_budget = float(input())
video_cards_count = int(input())
processor_count = int(input())
ram_memory_count = int(input())

video_cards_price = 250
processor_price = 0.35 * (video_cards_price * video_cards_count)
ram_memory_price = 0.10 * (video_cards_price * video_cards_count)

final_cost = video_cards_count * video_cards_price\
             + processor_count * processor_price\
             + ram_memory_count * ram_memory_price

if video_cards_count > processor_count:
    discount = 0.15 * final_cost
    final_cost -= discount

if petur_budget >= final_cost:
    left_budget = petur_budget - final_cost
    print(f"You have {left_budget:.2f} leva left!")
else:
    needed_money = final_cost - petur_budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
