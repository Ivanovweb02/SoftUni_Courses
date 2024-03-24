class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        message = ''
        if self.bullets > 0:
            self.bullets -= 1
            message = "shooting..."
        else:
            message = "no bullets left"
        return message

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


current_bullets = int(input())
weapon = Weapon(current_bullets)

print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
