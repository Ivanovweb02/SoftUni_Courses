# •	Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]

annual_fee = int(input())

# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

BASKETBALL_SHOES = annual_fee - (0.40 * annual_fee)
SPORT_OUTFIT = BASKETBALL_SHOES - (0.20 * BASKETBALL_SHOES)
BASKETBALL_BALL = 1 / 4 * SPORT_OUTFIT
BASKETBALL_ACCESSORIES = 1 / 5 * BASKETBALL_BALL

expenses_for_a_year = annual_fee \
                      + BASKETBALL_SHOES \
                      + SPORT_OUTFIT \
                      + BASKETBALL_BALL \
                      + BASKETBALL_ACCESSORIES

print(expenses_for_a_year)
