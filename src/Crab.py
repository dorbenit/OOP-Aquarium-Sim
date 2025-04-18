from Animal import Animal

class Crab(Animal):
    """
    Represents a crab in the aquarium.
    Crabs can only move horizontally.
    """

    def __init__(self, name, age, x, y, directionH):
        """
        Initializes a Crab object with basic animal properties.

        Args:
            name (str): Name of the crab.
            age (int): Age in steps (0–120).
            x (int): X-axis position.
            y (int): Y-axis position.
            directionH (int): Horizontal direction (0 for left, 1 for right).
        """
        super().__init__(name, age, x, y, directionH)

    def move(self):
        """
        Moves the crab one step horizontally based on its direction.
        """
        if self.directionH == 0:
            self.x -= 1
        elif self.directionH == 1:
            self.x += 1