some_string = input()
stack = []

for index in range(len(some_string)):
    char = some_string[index]
    if char == '(':
        stack.append(index)
    elif char == ')':
        start_index = stack.pop()
        end_index = index + 1
        print(some_string[start_index:end_index])
