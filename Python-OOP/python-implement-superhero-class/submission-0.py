class SuperHero:
    """Represents a superhero character with combat capabilities."""

    def __init__(self, name: str, power: str, health: int, attack_power: int) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.attack_power = attack_power
        # just Initialized name, power, health, and attack_power on self

    def attack(self, target: "SuperHero") -> None: # putted object as an atribute inside a method
        target.health-=self.attack_power         #  Decreased target's health by self.attack_power

        print(f"{self.name}. used {self.power} on {target.name} for {self.attack_power} damage!")
        # Printed f"{self.name} used {self.power} on {target.name} for {self.attack_power} damage!"
        

    def heal(self, amount: int) -> None:
        self.health += amount # Increased self.health by amount
        print(f"{self.name} healed for {amount} HP! Current health: {self.health}")
        

    def is_alive(self) -> bool:
        return self.health > 0
            
        
        #  Returning True if self.health > 0, else return False
        


# --- Test Cases ---
if __name__ == "__main__":
    hero1 = SuperHero("Iron Man", "Repulsor Beams", 100, 25)
    hero2 = SuperHero("Thanos", "Titan Strike", 120, 30)

    hero1.attack(hero2)
    print(f"Thanos health: {hero2.health}")

    hero2.attack(hero1)
    print(f"Iron Man health: {hero1.health}")

    hero1.heal(15)
    print(f"Is Iron Man alive? {hero1.is_alive()}")