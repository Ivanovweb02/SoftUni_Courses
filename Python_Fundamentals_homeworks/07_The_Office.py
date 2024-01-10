def office_happiness(some_list: list, some_factor: int):
    improvement_happiness = [happiness*some_factor for happiness in some_list]
    average_happiness = sum(improvement_happiness) / len(improvement_happiness)
    happy_employees = sum(happy_people >= average_happiness for happy_people in improvement_happiness)
    people_count = len(improvement_happiness)
    message = 'happy' if happy_employees >= people_count/2 else 'not happy'
    result = f"Score: {happy_employees}/{people_count}. Employees are {message}!"
    return result


employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())
print(office_happiness(employees_happiness, improvement_factor))
