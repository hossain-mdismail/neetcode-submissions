class SuperHero:
    """Represents a hero with customizable abilities and combat interactions."""

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.abilities: list[str] = []

    def add_ability(self, ability: str) -> None:
        self.abilities.append(ability)

    def use_ability(self, ability: str, target: "SuperHero", damage: int) -> None:
        if ability in self.abilities:
            target.health -= damage
            print(f"{self.name} used {ability} on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} doesn't know {ability}!")


# --- Test Cases ---
if __name__ == "__main__":
    hero1 = SuperHero("Doctor Strange", 100)
    hero2 = SuperHero("Dormammu", 300)

    hero1.add_ability("Mirror Dimension")
    hero1.add_ability("Time Loop")

    hero1.use_ability("Mirror Dimension", hero2, 50)
    print(f"Dormammu health: {hero2.health}")

    hero1.use_ability("Lightning Strike", hero2, 40)
    print(f"Dormammu health: {hero2.health}")