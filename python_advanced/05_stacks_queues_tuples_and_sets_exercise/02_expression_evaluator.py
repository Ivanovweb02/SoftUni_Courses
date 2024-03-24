import math
from collections import deque

sequence_of_operation = deque(input().split())
operation_numbers = deque()

final_result = 0
while sequence_of_operation:
    curr_result = 0
    curr_string = sequence_of_operation.popleft()
    if curr_string in ["*", "+", "-", "/"]:
        operator = curr_string
        curr_result = operation_numbers.popleft()
        while operation_numbers:
            if operator == '+':
                curr_result += operation_numbers.popleft()
            elif operator == '-':
                curr_result -= operation_numbers.popleft()
            elif operator == '*':
                curr_result *= operation_numbers.popleft()
            elif operator == '/':
                curr_result /= operation_numbers.popleft()
                curr_result = math.floor(curr_result)
        sequence_of_operation.appendleft(str(curr_result))
        final_result = curr_result
    else:
        curr_string = int(curr_string)
        operation_numbers.append(curr_string)

print(final_result)
