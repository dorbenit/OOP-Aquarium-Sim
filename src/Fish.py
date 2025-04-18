from Animal import Animal
from Exceptions import InvalidInputException

class Fish(Animal):
    """
    Represents a fish in the aquarium, extending the Animal class with vertical movement.
    """

    def __init__(self, name, age, x, y, directionH, directionV):
        """
        Initializes a Fish object with both horizontal and vertical directions.

        Args:
            name (str): Name of the fish.
            age (int): Age of the fish (0–120).
            x (int): X-axis position.
            y (int): Y-axis position.
            directionH (int): Horizontal direction (0 for left, 1 for right).
            directionV (int): Vertical direction (0 for down, 1 for up).

        Raises:
            InvalidInputException: If the vertical direction is not valid.
        """
        super().__init__(name, age, x, y, directionH)
        if directionV not in [0, 1] or not isinstance(directionV, int):
            raise InvalidInputException
        self.directionV = directionV

    def get_directionV(self):
        """
        Returns the vertical direction of the fish.
        """
        return self.directionV

    def set_directionV(self, directionV):
        """
        Sets the vertical direction of the fish.
        """
        self.directionV = directionV

    def move(self):
        """
        Moves the fish one step based on its horizontal and vertical direction.
        """
        if self.directionH == 0:
            self.x -= 1
        elif self.directionH == 1:
            self.x += 1
        if self.directionV == 0:
            self.y += 1
        elif self.directionV == 1:
            self.y -= 1
