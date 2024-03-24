some_password = input()
instruction = input()

while instruction != 'Done':
    instruction = instruction.split()
    command = instruction[0]
    if command == 'TakeOdd':
        new_password = ''
        for index in range(len(some_password)):
            if index % 2 != 0:
                new_password += some_password[index]
        some_password = new_password
        print(new_password)
    elif command == 'Cut':
        index = int(instruction[1])
        length = int(instruction[2])
        some_password = some_password[:index] + "" + some_password[(length + index):]
        print(some_password)
    elif command == 'Substitute':
        substring = instruction[1]
        substitute = instruction[2]
        if substring in some_password:
            some_password = some_password.replace(substring, substitute)
            print(some_password)
        else:
            print("Nothing to replace!")

    instruction = input()

print(f"Your password is: {some_password}")
