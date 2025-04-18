from Crab import Crab
import copy

ocypode = [[" ", "*", " ", " ", " ", "*", " "],
           [" ", " ", "*", "*", "*", " ", " "],
           ["*", "*", "*", "*", "*", "*", "*"],
           ["*", " ", " ", " ", " ", " ", "*"]]

class Ocypode(Crab):
    """
    Represents an Ocypode (ghost crab) in the aquarium.
    Inherits horizontal-only movement from the Crab class.
    """

    def __init__(self, name, age, x, y, directionH):
        """
        Initializes an Ocypode crab with dimensions and direction.

        Args:
            name (str): Name of the Ocypode.
            age (int): Age of the crab.
            x (int): X-axis location.
            y (int): Y-axis location.
            directionH (int): Horizontal direction (0 for left, 1 for right).
        """
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 4

    def get_animal(self):
        """
        Returns the static 2D shape of the Ocypode crab.

        Returns:
            list[list[str]]: Shape matrix.
        """
        return copy.deepcopy(ocypode)