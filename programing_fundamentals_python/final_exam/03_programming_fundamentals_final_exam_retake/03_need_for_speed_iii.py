number_of_cars = int(input())
car_garage = {}
for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    car_garage[car] = {}
    car_garage[car]['mileage'] = int(mileage)
    car_garage[car]['fuel'] = int(fuel)

instructions = input()
while instructions != 'Stop':
    instructions = instructions.split(" : ")
    command = instructions[0]
    if command == 'Drive':
        car = instructions[1]
        distance = int(instructions[2])
        fuel = int(instructions[3])
        if car_garage[car]['fuel'] >= fuel:
            car_garage[car]['mileage'] += distance
            car_garage[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_garage[car]['mileage'] >= 100_000:
                del car_garage[car]
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    elif command == 'Refuel':
        car = instructions[1]
        fuel = int(instructions[2])
        if car_garage[car]['fuel'] + fuel > 75:
            diff = 75 - car_garage[car]['fuel']
            car_garage[car]['fuel'] += diff
            print(f"{car} refueled with {diff} liters")
        else:
            car_garage[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        car = instructions[1]
        kilometers = int(instructions[2])
        if (car_garage[car]['mileage'] - kilometers) < 10_000:
            car_garage[car]['mileage'] = 10_000
        else:
            car_garage[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    instructions = input()

for car in car_garage.keys():
    print(f"{car} -> Mileage: {car_garage[car]['mileage']} kms, Fuel in the tank: {car_garage[car]['fuel']} lt.")
