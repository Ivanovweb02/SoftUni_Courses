country = input()
tool = input()

difficulty = 0
execution = 0

if country == "Russia":
    if tool == "ribbon":
        difficulty = 9.100
        execution = 9.400
    elif tool == "hoop":
        difficulty = 9.300
        execution = 9.800
    elif tool == "rope":
        difficulty = 9.600
        execution = 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        difficulty = 9.600
        execution = 9.400
    elif tool == "hoop":
        difficulty = 9.550
        execution = 9.750
    elif tool == "rope":
        difficulty = 9.500
        execution = 9.400
elif country == "Italy":
    if tool == "ribbon":
        difficulty = 9.200
        execution = 9.500
    elif tool == "hoop":
        difficulty = 9.450
        execution = 9.350
    elif tool == "rope":
        difficulty = 9.700
        execution = 9.150

total_point = difficulty + execution
needed_point = (20 - total_point)
needed_point_percent = (needed_point / 20) * 100
print(f"The team of {country} get {total_point :.3f} on {tool}.")
print(f"{needed_point_percent :.2f}%")
