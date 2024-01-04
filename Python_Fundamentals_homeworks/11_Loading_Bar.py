def loading(some_number: int) -> str:
    loading_bar = []
    if some_number == 100:
        return f"{some_number}% Complete!\n[%%%%%%%%%%]"
    percents = some_number // 10
    return f"{some_number}% [{'%' * percents}{'.' * (10 - percents)}]\nStill loading..."


number = int(input())
print(loading(number))
