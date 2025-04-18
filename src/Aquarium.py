from Exceptions import InvalidAnimalType, NotAvailablePlace, TooSmallAquariumSize, InvalidInputException
from Molly import Molly
from Ocypode import Ocypode
from Scalar import Scalar
from Shrimp import Shrimp
from Crab import Crab
from Fish import Fish

class Aquarium:
    """
    A 2D aquarium simulation environment. Handles creation of animals, their movement,
    interaction with the environment (walls, collisions), and time-based logic (age, hunger).
    """

    def __init__(self, aqua_width, aqua_height):
        """
        Initializes the aquarium with a given width and height.
        Validates that the aquarium meets minimum required dimensions.

        Raises:
            InvalidInputException: If dimensions are not integers.
            TooSmallAquariumSize: If dimensions are too small.
        """
        if not isinstance(aqua_width, int):
            raise InvalidInputException
        if aqua_width < 40:
            raise TooSmallAquariumSize
        if not isinstance(aqua_height, int):
            raise InvalidInputException
        if aqua_height < 25:
            raise TooSmallAquariumSize

        self.aqua_width = aqua_width
        self.aqua_height = aqua_height
        self.step = 0
        self.animals = []

        # Build initial aquarium board
        board = []
        for y in range(self.aqua_height - 1):
            if y == 2:
                board.append(['|'] + ['~' for _ in range(self.aqua_width - 2)] + ['|'])
            else:
                board.append(['|'] + [' ' for _ in range(self.aqua_width - 2)] + ['|'])
        board.append(['\\'] + ['_' for _ in range(self.aqua_width - 2)] + ['/'])
        self.board = board

    def __str__(self):
        """
        Returns a summary of the aquarium and all current animals.
        """
        aquarium_description = f"The aquarium, sized {self.aqua_height}/{self.aqua_width} and currently in step {self.step}, contains the following animals:\n"
        animals_description = ""
        for animal in self.animals:
            animals_description += f"The {animal.__class__.__name__.lower()} {animal.name} is {animal.age} years old and has {animal.food} food.\n"
        return aquarium_description + animals_description

    def feed_all(self):
        """
        Feeds all animals in the aquarium by adding 10 food units to each.
        """
        for animal in self.animals:
            animal.add_food(10)

    def __repr__(self):
        """
        Returns the visual (textual) representation of the aquarium board.
        """
        board_str = ""
        for row in self.board:
            board_str += ' '.join(row) + '\n'
        return board_str

    def __insert_animal_to_board(self, animal):
        """
        Places an animal's shape onto the board based on its position.

        Args:
            animal: The animal object to draw on the board.
        """
        animal_shape = animal.get_animal()
        animal_height = animal.get_size()[1]
        animal_width = animal.get_size()[0]
        for i in range(animal_height):
            for j in range(animal_width):
                if animal_shape[i][j] != ' ':
                    self.board[animal.y + i][animal.x + j] = animal_shape[i][j]

    def __delete_animal_from_board(self, animal):
        """
        Erases the animal's shape from the board.

        Args:
            animal: The animal object to erase.
        """
        animal_shape = animal.get_animal()
        animal_height = animal.get_size()[1]
        animal_width = animal.get_size()[0]
        for i in range(animal_height):
            for j in range(animal_width):
                if animal_shape[i][j] != ' ':
                    self.board[animal.y + i][animal.x + j] = " "

    def is_valid(self, animal):
        """
        Checks if the animal can be placed without overlapping other animals.

        Raises:
            NotAvailablePlace: If the animal's intended location is already occupied.
        """
        animal_height = animal.get_size()[1]
        animal_width = animal.get_size()[0]

        # Adjust out-of-bounds positions
        if animal.x > (self.aqua_width - animal_width - 1):
            animal.x = (self.aqua_width - animal_width - 1)

        if isinstance(animal, Crab):
            animal.y = (self.aqua_height - animal_height - 1)
        elif animal.y > (self.aqua_height - 5 - animal_height):
            animal.y = (self.aqua_height - 5 - animal_height)
        elif animal.y < 3:
            animal.y = 3

        # Create temporary board to check for collisions
        temp_aquarium = []
        for y in range(self.aqua_height - 1):
            if y == 2:
                temp_aquarium.append(['|'] + ['~' for _ in range(self.aqua_width - 2)] + ['|'])
            else:
                temp_aquarium.append(['|'] + [' ' for _ in range(self.aqua_width - 2)] + ['|'])
        temp_aquarium.append(['\\'] + ['_' for _ in range(self.aqua_width - 2)] + ['/'])

        for old_animal in self.animals:
            for i in range(old_animal.get_size()[1]):
                for j in range(old_animal.get_size()[0]):
                    temp_aquarium[old_animal.y + i][old_animal.x + j] = '*'

        for i in range(animal.get_size()[1]):
            for j in range(animal.get_size()[0]):
                if temp_aquarium[animal.y + i][animal.x + j] == '*':
                    raise NotAvailablePlace

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        """
        Adds a new animal to the aquarium.

        Raises:
            InvalidInputException: If the type is not a string.
            InvalidAnimalType: If the type is unknown.
        """
        if not isinstance(animaltype, str):
            raise InvalidInputException
        if animaltype not in ["ocypode", "molly", "scalar", "shrimp"]:
            raise InvalidAnimalType(animaltype)

        if animaltype == "ocypode":
            animal = Ocypode(name, age, x, y, directionH)
        elif animaltype == "molly":
            animal = Molly(name, age, x, y, directionH, directionV)
        elif animaltype == "scalar":
            animal = Scalar(name, age, x, y, directionH, directionV)
        elif animaltype == "shrimp":
            animal = Shrimp(name, age, x, y, directionH)

        self.is_valid(animal)
        self.animals.append(animal)
        self.__insert_animal_to_board(animal)

    def __kill_animal(self, animal):
        """
        Removes the animal if it dies from age or starvation.
        """
        if animal.die() or animal.starvation():
            self.__delete_animal_from_board(animal)
            self.animals.remove(animal)

    def check_if_colide(self):
        """
        Detects collisions with walls or between animals and changes direction accordingly.
        """
        for animal in self.animals:
            animal_height = animal.get_size()[1]
            animal_width = animal.get_size()[0]
            if isinstance(animal, Fish):
                if animal.y == 3 and animal.directionV == 1:
                    animal.directionV = 0
                if animal.y == self.aqua_height - 5 - animal_height and animal.directionV == 0:
                    animal.directionV = 1
                if animal.x == 1 and animal.directionH == 0:
                    animal.directionH = 1
                if animal.x == self.aqua_width - 1 - animal_width and animal.directionH == 1:
                    animal.directionH = 0
            else:
                if animal.x == 1 and animal.directionH == 0:
                    animal.directionH = 1
                if animal.x == self.aqua_width - 1 - animal_width and animal.directionH == 1:
                    animal.directionH = 0

        for i in range(len(self.animals)):
            crab1 = self.animals[i]
            if isinstance(crab1, Crab):
                for j in range(i + 1, len(self.animals)):
                    crab2 = self.animals[j]
                    if isinstance(crab2, Crab):
                        if crab1.directionH == 1 and crab2.directionH == 0 and crab1.x < crab2.x and (crab2.x - crab1.x) < 9:
                            crab1.directionH = 0
                            crab2.directionH = 1
                        elif crab2.directionH == 1 and crab1.directionH == 0 and crab2.x < crab1.x and (crab1.x - crab2.x) < 9:
                            crab2.directionH = 0
                            crab1.directionH = 1

    def next_step(self):
        """
        Advances the simulation by one time step.
        Handles: rebuilding the board, killing dead animals, moving, and aging.
        """
        self.step += 1

        # Reset the board
        board = []
        for y in range(self.aqua_height - 1):
            if y == 2:
                board.append(['|'] + ['~' for _ in range(self.aqua_width - 2)] + ['|'])
            else:
                board.append(['|'] + [' ' for _ in range(self.aqua_width - 2)] + ['|'])
        board.append(['\\'] + ['_' for _ in range(self.aqua_width - 2)] + ['/'])
        self.board = board

        # Update animals
        for animal in self.animals:
            self.__kill_animal(animal)
        self.check_if_colide()
        for animal in self.animals:
            animal.move()
        for animal in self.animals:
            self.__insert_animal_to_board(animal)

        # Apply food and age updates every 10 steps
        if self.step % 10 == 0:
            for animal in self.animals:
                animal.dec_food()
                animal.age += 1

    def several_steps(self, steps):
        """
        Runs the simulation for multiple steps.

        Args:
            steps (int): Number of steps to simulate.
        """
        for _ in range(steps):
            self.next_step()
