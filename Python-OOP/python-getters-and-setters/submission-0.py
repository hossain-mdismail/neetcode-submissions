class User:
    """Represents a user profile with validated age access."""

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self._age = 0
        self.age = age  # Uses the setter logic immediately

    @property
    def age(self) -> int:
        #  Return internal _age
        return self._age
        

    @age.setter
    def age(self, new_age: int) -> None:
        # Validate new_age >= 0 before updating _age
        if new_age >= 0:
            self._age = new_age


if __name__ == "__main__":
    user = User("Alice", 25)
    print(f"Username: {user.username}")
    print(f"Initial age: {user.age}")

    # Valid update
    user.age = 26
    print(f"Updated age: {user.age}")

    # Invalid update
    user.age = -5
    print(f"Age after invalid update: {user.age}")