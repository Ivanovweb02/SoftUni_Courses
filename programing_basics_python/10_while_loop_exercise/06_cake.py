width = int(input())
height = int(input())

size_of_cake = width * height
left_pieces = size_of_cake

command = input()
while command != "STOP":
    taken_pieces = int(command)
    left_pieces -= taken_pieces
    if left_pieces <= 0:
        break

    command = input()

if command == "STOP":
    print(f"{left_pieces} pieces are left.")
else:
    needed_pieces = abs(left_pieces)
    print(f"No more cake left! You need {needed_pieces} pieces more.")
