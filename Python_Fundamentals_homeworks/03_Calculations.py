def calculator(action, num_1, num_2):
    if action == 'subtract':
        return num_1 - num_2
    elif action == 'add':
        return num_1 + num_2
    elif action == 'divide':
        return int(num_1 / num_2)
    elif action == 'multiply':
        return num_1 * num_2


operation = input()
first_number = int(input())
second_number = int(input())
print(calculator(operation, first_number, second_number))
