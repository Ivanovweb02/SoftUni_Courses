count_of_cargo = int(input())
price_per_ton = 0
total_tons = 0
van_cargo = 0
truck_cargo = 0
train_cargo = 0

for current_cargo in range(1, count_of_cargo + 1):
    ton_of_cargo = int(input())
    total_tons += ton_of_cargo
    if ton_of_cargo <= 3:
        van_cargo += ton_of_cargo
        price_per_ton += 200 * ton_of_cargo
    elif ton_of_cargo <= 11:
        truck_cargo += ton_of_cargo
        price_per_ton += 175 * ton_of_cargo
    else:
        train_cargo += ton_of_cargo
        price_per_ton += 120 * ton_of_cargo

avr_ton_of_cargo = price_per_ton / total_tons
percent_cargo_in_van = van_cargo / total_tons * 100
percent_cargo_in_truck = truck_cargo / total_tons * 100
percent_cargo_in_train = train_cargo / total_tons * 100
print(f"{avr_ton_of_cargo :.2f}")
print(f"{percent_cargo_in_van :.2f}%")
print(f"{percent_cargo_in_truck :.2f}%")
print(f"{percent_cargo_in_train :.2f}%")
