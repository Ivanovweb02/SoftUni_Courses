junior_bikers_count = int(input())
senior_bikers_count = int(input())
type_of_route = input()

total_participators = junior_bikers_count + senior_bikers_count
cost_of_route_per_juniors = 0
cost_of_route_per_seniors = 0

if type_of_route == "trail":
    cost_of_route_per_juniors = 5.50 * junior_bikers_count
    cost_of_route_per_seniors = 7 * senior_bikers_count

elif type_of_route == "cross-country":
    cost_of_route_per_juniors = 8 * junior_bikers_count
    cost_of_route_per_seniors = 9.50 * senior_bikers_count
    if total_participators >= 50:
        cost_of_route_per_juniors -= cost_of_route_per_juniors * 0.25
        cost_of_route_per_seniors -= cost_of_route_per_seniors * 0.25

elif type_of_route == "downhill":
    cost_of_route_per_juniors = 12.25 * junior_bikers_count
    cost_of_route_per_seniors = 13.75 * senior_bikers_count

elif type_of_route == "road":
    cost_of_route_per_juniors = 20 * junior_bikers_count
    cost_of_route_per_seniors = 21.50 * senior_bikers_count

money_collected = cost_of_route_per_seniors + cost_of_route_per_juniors
expenses = money_collected * 0.05
money_collected -= expenses

print(f"{money_collected :.2f}")
