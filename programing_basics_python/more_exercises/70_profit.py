count_one_lev = int(input())
count_two_lev = int(input())
count_five_lev = int(input())
amount = int(input())

for one_lev_coin in range(count_one_lev + 1):
    for two_lev_coin in range(count_two_lev + 1):
        for five_lev_banknote in range(count_five_lev + 1):
            if (one_lev_coin * 1) + (two_lev_coin * 2) + (five_lev_banknote * 5) == amount:
                print(f'{one_lev_coin} * 1 lv. + {two_lev_coin} * 2 lv. + {five_lev_banknote} * 5 lv. = {amount} lv.')
