def integer(some_num: int) -> int:
    some_num *= 2
    return some_num


def real(some_num: float) -> str:
    some_num *= 1.5
    return f"{some_num :.2f}"


def string(some_text: str) -> str:
    return f"${some_text}$"


data_type = input()
number = input()

if data_type == 'int':
    number = int(number)
    print(integer(number))

elif data_type == 'real':
    number = float(number)
    print(real(number))

elif data_type == 'string':
    print(string(number))
