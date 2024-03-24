class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        result = Circle.__pi * self.diameter
        return result

    def calculate_area(self):
        result = Circle.__pi * self.radius**2
        return result

    def calculate_area_of_sector(self, angle):
        result = Circle.__pi * self.radius**2 * (angle/360)
        return result


current_diameter = int(input())
circle = Circle(current_diameter)
current_angle = int(input())

print(f"{circle.calculate_circumference() :.2f}")
print(f"{circle.calculate_area() :.2f}")
print(f"{circle.calculate_area_of_sector(current_angle) :.2f}")
