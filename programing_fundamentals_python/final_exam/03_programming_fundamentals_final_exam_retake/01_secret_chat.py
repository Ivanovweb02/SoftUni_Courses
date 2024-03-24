concealed_message = input()
instruction = input()

while instruction != 'Reveal':
    instruction = instruction.split(":|:")
    command = instruction[0]
    if command == 'InsertSpace':
        index = int(instruction[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
    elif command == 'Reverse':
        substring = instruction[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
        else:
            print('error')
            instruction = input()
            continue
    elif command == 'ChangeAll':
        substring = instruction[1]
        replacement = instruction[2]
        concealed_message = concealed_message.replace(substring, replacement)
    print(concealed_message)

    instruction = input()

print(f"You have a new text message: {concealed_message}")
