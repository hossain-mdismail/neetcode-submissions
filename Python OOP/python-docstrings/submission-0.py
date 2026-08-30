class SuperHero:
    # TODO: Add a docstring describing the SuperHero class:
    # "A class to represent a superhero character."
    
    def __init__(self, name: str, power: str, strength: int) -> None:
        # TODO: Add a docstring describing this constructor:
        # "Initialize a superhero with name, power, and strength attributes."
        self.name = name
        self.power = power
        self.strength = strength

    def describe(self) -> str:
        # TODO: Add a docstring describing this method:
        # "Return a string describing the hero's power and strength."
        return f"{self.name} wields {self.power} with {self.strength} strength!"


# Test cases - Run the script to verify
hero = SuperHero("Thor", "Thunder", 95)
print(hero.describe())
print("Class docstring:", SuperHero.__doc__)
print("Init docstring:", SuperHero.__init__.__doc__)
print("Describe docstring:", SuperHero.describe.__doc__)