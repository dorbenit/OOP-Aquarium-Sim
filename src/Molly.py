from Fish import Fish
molly_left = [[" ", "*", "*", "*", "*", " ", " ", "*"],
              ["*", "*", "*", "*", "*", "*", "*", "*"],
              [" ", "*", "*", "*", "*", " ", " ", "*"]]

molly_right = [["*", " ", " ", "*", "*", "*", "*", " "],
               ["*", "*", "*", "*", "*", "*", "*", "*"],
               ["*", " ", " ", "*", "*", "*", "*", " "]]
import copy

class Molly(Fish):
    """
    Represents a Molly fish with a fixed graphical representation
    depending on its horizontal direction.
    """

    def __init__(self, name, age, x, y, directionH, directionV):
        """
        Initializes a Molly fish object with name, age, position, and direction.

        Args:
            name (str): Name of the Molly.
            age (int): Age of the fish.
            x (int): X-axis position.
            y (int): Y-axis position.
            directionH (int): Horizontal direction (0 for left, 1 for right).
            directionV (int): Vertical direction (0 for down, 1 for up).
        """
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 3

    def get_animal(self):
        """
        Returns the 2D representation of the Molly based on its horizontal direction.

        Returns:
            list[list[str]]: A deep copy of the shape matrix.
        """
        if self.directionH == 0:
            return copy.deepcopy(molly_left)
        elif self.directionH == 1:
            return copy.deepcopy(molly_right)