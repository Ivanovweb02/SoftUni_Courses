total_steps = 0

command = input()
while command != "Going home":
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= 10000:
        break

    command = input()

if command == "Going home":
    current_steps = int(input())
    total_steps += current_steps

if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - total_steps} more steps to reach goal.")
