number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0

type_of_number = ""

if operator == "+":
    result = number_1 + number_2
elif operator == "-":
    result = number_1 - number_2
elif operator == "*":
    result = number_1 * number_2
elif operator == "/" and number_2 != 0:
    result = number_1 / number_2
    result = f"{result:.2f}"
elif (operator == "/" or operator == "%") and number_2 == 0:
    print(f"Cannot divide {number_1} by zero")
elif operator == "%":
    result = number_1 % number_2

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        type_of_number = "even"
    else:
        type_of_number = "odd"
    print(f"{number_1} {operator} {number_2} = {result} - {type_of_number}")

elif (operator == "/" or operator == "%") and number_2 != 0:
    print(f"{number_1} {operator} {number_2} = {result}")
