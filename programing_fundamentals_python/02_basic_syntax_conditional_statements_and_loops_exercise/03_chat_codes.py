number = int(input())
message = ""

for _ in range(number):
    current_number = int(input())
    if current_number == 88:
        message = "Hello"
    elif current_number == 86:
        message = "How are you?"
    elif current_number < 88:
        message = "GREAT!"
    elif current_number > 88:
        message = "Bye."
    print(message)
