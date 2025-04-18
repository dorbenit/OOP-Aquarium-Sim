from Crab import Crab
import copy

shrimp_left = [["*", " ", "*", " ", " ", " ", " "],
               [" ", "*", "*", "*", "*", "*", "*"],
               [" ", " ", "*", " ", "*", " ", " "]]

shrimp_right = [[" ", " ", " ", " ", "*", " ", "*"],
                ["*", "*", "*", "*", "*", "*", " "],
                [" ", " ", "*", " ", "*", " ", " "]]

class Shrimp(Crab):
    """
    Represents a Shrimp in the aquarium.
    Inherits horizontal-only movement from the Crab class and includes a visual representation.
    """

    def __init__(self, name, age, x, y, directionH):
        """
        Initializes a Shrimp with position, direction, and shape dimensions.

        Args:
            name (str): Name of the shrimp.
            age (int): Age in simulation steps.
            x (int): X-axis location.
            y (int): Y-axis location.
            directionH (int): Horizontal direction (0 for left, 1 for right).
        """
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 3

    def get_animal(self):
        """
        Returns the 2D visual representation of the shrimp based on its direction.

        Returns:
            list[list[str]]: Shape matrix of the shrimp.
        """
        if self.directionH == 0:
            return copy.deepcopy(shrimp_left)
        elif self.directionH == 1:
            return copy.deepcopy(shrimp_right)
