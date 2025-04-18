from unittest import TestCase
from Molly import Molly
from Exceptions import InvalidInputException
molly_left = [[" ", "*", "*", "*", "*", " ", " ", "*"],
              ["*", "*", "*", "*", "*", "*", "*", "*"],
              [" ", "*", "*", "*", "*", " ", " ", "*"]]

molly_right = [["*", " ", " ", "*", "*", "*", "*", " "],
               ["*", "*", "*", "*", "*", "*", "*", "*"],
               ["*", " ", " ", "*", "*", "*", "*", " "]]
class TestMolly(TestCase):
    def test_molly_initialization(self):
        molly = Molly("Molly1", 5, 10, 15, 1, 0)
        self.assertEqual(molly.name, "Molly1")
        self.assertEqual(molly.age, 5)
        self.assertEqual(molly.x, 10)
        self.assertEqual(molly.y, 15)
        self.assertEqual(molly.directionH, 1)
        self.assertEqual(molly.directionV, 0)

    def test_invalid_age(self):
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", -1, 10, 15, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", 121, 10, 15, 1, 0)

    def test_molly_invalid_name(self):
        with self.assertRaises(InvalidInputException):
            Molly("", 10, 10, 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly(123, 10, 10, 10, 1, 0)

    def test_molly_invalid_coordinates(self):
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", 10, -1, 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", 10, 10, -1, 1, 0)
            Molly("MollyTest", 10, "x", 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", 10, 10, "y", 1, 0)

    def test_molly_invalid_directionH(self):
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", 10, 10, 10, -1, 0)
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", 10, 10, 10, 2, 0)
        with self.assertRaises(InvalidInputException):
            Molly("MollyTest", 10, 10, 10, "direction", 0)

    def test_get_animal(self):
        molly = Molly("Molly1", 1, 10, 15, 0, 0)
        self.assertEqual(molly.get_animal(), molly_left)
        molly.set_directionH(1)
        self.assertEqual(molly.get_animal(), molly_right)

    def test_starvation(self):
        molly = Molly("Molly1", 5, 10, 15, 1, 0)
        self.assertFalse(molly.starvation())
        molly.food = 0
        self.assertTrue(molly.starvation())

    def test_die(self):
        molly = Molly("Molly1", 5, 10, 15, 1, 0)
        self.assertFalse(molly.die())
        molly.age = 120
        self.assertTrue(molly.die())


    def test_str(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        expected_str = "The molly MollyTest is 10 years old and has 10 food."
        self.assertEqual(str(molly), expected_str)

    def test_repr(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        molly.directionH = 1
        animal_shape = molly_right
        animal_str = ""
        for row in animal_shape:
            animal_str += " ".join(row) + '\n'
        animal_str = animal_str.rstrip("\n")
        self.assertEqual(repr(molly), animal_str)

    def test_get_position(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        self.assertEqual(molly.get_position(), (5, 5))

    def test_get_directionH(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        self.assertEqual(molly.get_directionH(), 1)

    def test_get_size(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        self.assertEqual(molly.get_size(), (8, 3))

    def test_dec_food(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        molly.dec_food()
        self.assertEqual(molly.food, 9)

    def test_add_food(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        molly.add_food(5)
        self.assertEqual(molly.food, 15)

    def test_inc_age(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        molly.inc_age()
        self.assertEqual(molly.age, 11)

    def test_set_directionH(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        molly.set_directionH(0)
        self.assertEqual(molly.directionH, 0)



    def test_move(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        molly.set_directionH(1)
        molly.set_directionV(0)
        molly.move()
        self.assertEqual(molly.get_position(), (6, 6))

        molly.set_directionH(0)
        molly.set_directionV(1)
        molly.move()
        self.assertEqual(molly.get_position(), (5, 5))

    def test_set_directionV(self):
        molly = Molly("MollyTest", 10, 5, 5, 1, 0)
        molly.set_directionV(0)
        self.assertEqual(molly.directionV, 0, "Failed to set directionV to down (0)")
        molly.set_directionV(1)
        self.assertEqual(molly.directionV, 1, "Failed to set directionV to up (1)")

    def test_get_directionV(self):
        molly = Molly("TestMolly", 1, 2, 3, 1, 0)
        self.assertEqual(molly.get_directionV(), 0, "Initial vertical direction should be 0")
        molly.set_directionV(1)
        self.assertEqual(molly.get_directionV(), 1, "Vertical direction should be updated to 1")


