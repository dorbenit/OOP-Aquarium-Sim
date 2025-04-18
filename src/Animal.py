from abc import ABC, abstractmethod
from Exceptions import InvalidInputException


class Animal(ABC):
    """
    Abstract base class for all animals in the aquarium.
    Handles common properties such as name, age, position, direction, and food level.
    """

    def __init__(self, name, age, x, y, directionH):
        """
        Initializes the base Animal object with name, age, position, and horizontal direction.

        Raises:
            InvalidInputException: If any of the provided inputs are invalid.
        """
        if not isinstance(name, str) or name == "":
            raise InvalidInputException
        self.name = name
        if not (0 < age < 120) or not isinstance(age, int):
            raise InvalidInputException
        self.age = age
        self.food = 10
        if not isinstance(x, int) or not isinstance(y, int) or x <= 0 or y <= 0:
            raise InvalidInputException
        self.x = x
        self.y = y
        if directionH not in [0, 1] or not isinstance(directionH, int):
            raise InvalidInputException
        self.directionH = directionH

    def __str__(self):
        """
        Returns a user-friendly string representation of the animal.
        """
        return f"The {self.__class__.__name__.lower()} {self.name} is {self.age} years old and has {self.food} food."

    @abstractmethod
    def get_animal(self):
        """
        Returns the 2D visual representation of the animal.
        Must be implemented by derived classes.
        """
        pass

    def __repr__(self):
        """
        Returns a string of the animal's 2D shape, formatted as rows of characters.
        """
        animal_shape = self.get_animal()
        animal_str = ""
        for row in animal_shape:
            animal_str += " ".join(row) + '\n'
        animal_str = animal_str.rstrip("\n")
        return animal_str

    def get_position(self):
        """
        Returns the current (x, y) position of the animal.
        """
        return (self.x, self.y)

    def get_directionH(self):
        """
        Returns the horizontal direction of the animal.
        """
        return self.directionH

    def get_size(self):
        """
        Returns the size of the animal as (width, height).
        """
        return (self.width, self.height)

    def dec_food(self):
        """
        Decreases the food level by 1.
        """
        self.food -= 1

    def add_food(self, amount):
        """
        Increases the food level by a given amount.
        """
        self.food += amount

    def inc_age(self):
        """
        Increases the animal's age by 1.
        """
        self.age += 1

    @abstractmethod
    def move(self):
        """
        Moves the animal based on its internal logic.
        Must be implemented by derived classes.
        """
        pass

    def set_directionH(self, directionH):
        """
        Sets the horizontal direction of the animal.
        """
        self.directionH = directionH

    def starvation(self):
        """
        Checks if the animal has no food left. If so, it is considered dead by starvation.

        Returns:
            bool: True if dead by starvation, False otherwise.
        """
        if self.food == 0:
            print(f"{self.name} died at the age of {self.age} years because it ran out of food.")
            return True
        else:
            return False

    def die(self):
        """
        Checks if the animal died of old age (age >= 120).

        Returns:
            bool: True if died of age, False otherwise.
        """
        if self.age >= 120:
            print(f"{self.name} died in a good health.")
            return True
        else:
            return False
