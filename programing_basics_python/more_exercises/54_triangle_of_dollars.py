number = int(input())

for start in range(1, number + 1):
    for _ in range(1, start + 1):
        print("$", end=" ")
    print("")
