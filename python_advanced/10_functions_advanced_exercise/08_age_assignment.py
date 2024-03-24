def age_assignment(*args, **kwargs):
    result = ''
    for key in sorted(kwargs.keys(), key=lambda x: x):
        for name in args:
            if key == name[0]:
                result += f"{name} is {kwargs[key]} years old.\n"
                break
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
