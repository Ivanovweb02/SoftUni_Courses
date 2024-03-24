count_of_command = int(input())
system_of_data = {}

for _ in range(count_of_command):
    data = input().split()
    command = data[0]
    if command == "register":
        username = data[1]
        license_plate_num = data[2]
        if username not in system_of_data:
            system_of_data[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_num}")

    elif command == 'unregister':
        username = data[1]
        if username not in system_of_data:
            print(f"ERROR: user {username} not found")
        else:
            del system_of_data[username]
            print(f"{username} unregistered successfully")

for (user, license_num) in system_of_data.items():
    print(f"{user} => {license_num}")
