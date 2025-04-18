from Fish import Fish
import copy

scalar_left = [[" ", " ", "*", "*", "*", "*", "*", "*"],
               [" ", "*", "*", "*", " ", " ", " ", " "],
               ["*", "*", "*", "*", "*", "*", " ", " "],
               [" ", "*", "*", "*", " ", " ", " ", " "],
               [" ", " ", "*", "*", "*", "*", "*", "*"]]

scalar_right = [["*", "*", "*", "*", "*", "*", " ", " "],
                [" ", " ", " ", " ", "*", "*", "*", " "],
                [" ", " ", "*", "*", "*", "*", "*", "*"],
                [" ", " ", " ", " ", "*", "*", "*", " "],
                ["*", "*", "*", "*", "*", "*", " ", " "]]

class Scalar(Fish):
    """
    Represents a Scalar fish in the aquarium.
    Has a unique 5x8 visual representation depending on direction.
    """

    def __init__(self, name, age, x, y, directionH, directionV):
        """
        Initializes a Scalar fish with dimensions, position, and direction.

        Args:
            name (str): Name of the Scalar.
            age (int): Age in simulation steps.
            x (int): X-axis location.
            y (int): Y-axis location.
            directionH (int): Horizontal direction (0 for left, 1 for right).
            directionV (int): Vertical direction (0 for down, 1 for up).
        """
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 5

    def get_animal(self):
        """
        Returns the 2D shape of the Scalar based on its direction.

        Returns:
            list[list[str]]: Shape matrix of the Scalar.
        """
        if self.directionH == 0:
            return copy.deepcopy(scalar_left)
        elif self.directionH == 1:
            return copy.deepcopy(scalar_right)
