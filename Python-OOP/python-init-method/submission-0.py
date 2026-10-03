class SuperHero:
    def __init__(self, name: str, power: str, health: int, speed: int) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        print(f"{self.name} took {damage} damage! Remaining health: {self.health}")

    def is_alive(self) -> bool:
        return self.health > 0


# Test cases
batman = SuperHero("Batman", "Martial Arts", 100, 75)
print(batman.name)
batman.take_damage(30)
print(f"Is Batman alive? {batman.is_alive()}")
