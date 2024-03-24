encrypted_message = input()

instruction = input()
while instruction != 'Decode':
    instruction = instruction.split('|')
    command = instruction[0]
    if command == 'Move':
        number_of_letters = int(instruction[1])
        removed_letters = []
        for index in range(0, number_of_letters):
            removed_letters.append(encrypted_message[index])
        for letter in removed_letters:
           encrypted_message = encrypted_message.replace(letter, "", 1)
        for letter in removed_letters:
            encrypted_message += letter
    elif command == 'Insert':
        index = int(instruction[1])
        value = instruction[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command == 'ChangeAll':
        substring = instruction[1]
        replacement = instruction[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    instruction = input()

print(f"The decrypted message is: {encrypted_message}")
