import unittest
from Aquarium import Aquarium
from Exceptions import InvalidAnimalType

class TestAquarium(unittest.TestCase):

    def setUp(self):
        self.aquarium = Aquarium(45, 27)

    def test_add_animals(self):
        self.aquarium.add_animal("Shrimpy", 10, 5, 3, 1, 0, "shrimp")
        self.aquarium.add_animal("Scaly", 12, 10, 4, 0, 1, "scalar")
        self.assertEqual(len(self.aquarium.animals), 2)

    def test_repr_board_structure(self):
        board_str = repr(self.aquarium)
        self.assertTrue(isinstance(board_str, str))
        self.assertGreater(len(board_str), 0)

    def test_str_summary(self):
        self.aquarium.add_animal("Testy", 15, 3, 3, 0, 0, "ocypode")
        summary = str(self.aquarium)
        self.assertIn("Testy", summary)
        self.assertIn("ocypode", summary.lower())

    def test_several_steps_progression(self):
        self.aquarium.add_animal("Mover", 20, 1, 3, 1, 0, "molly")
        old_position = self.aquarium.animals[0].get_position()
        self.aquarium.several_steps(5)
        new_position = self.aquarium.animals[0].get_position()
        self.assertNotEqual(old_position, new_position)

    def test_invalid_animal_type(self):
        with self.assertRaises(InvalidAnimalType):
            self.aquarium.add_animal("Ghosty", 10, 5, 5, 0, 0, "ghost")

    def test_food_and_age_updates(self):
        self.aquarium.add_animal("Aged", 10, 5, 3, 1, 1, "molly")
        molly = self.aquarium.animals[0]
        initial_food = molly.food
        initial_age = molly.age
        self.aquarium.several_steps(10)
        self.assertEqual(molly.food, initial_food - 1)
        self.assertEqual(molly.age, initial_age + 1)

    def test_starvation_removal(self):
        self.aquarium.add_animal("Hungry", 10, 5, 3, 1, 1, "molly")
        molly = self.aquarium.animals[0]
        molly.food = 0  # manually starve
        self.aquarium.next_step()
        self.assertNotIn(molly, self.aquarium.animals)

    def test_old_age_death(self):
        self.aquarium.add_animal("Oldie", 119, 5, 3, 1, 1, "scalar")
        scalar = self.aquarium.animals[0]
        self.aquarium.several_steps(11)  # should age and die
        self.assertNotIn(scalar, self.aquarium.animals)

    def test_collision_handling(self):
        # Two crabs heading toward each other
        self.aquarium.add_animal("Lefty", 10, 10, 20, 1, 0, "ocypode")
        self.aquarium.add_animal("Righty", 10, 18, 20, 0, 0, "ocypode")
        for _ in range(3):
            self.aquarium.next_step()
        # Check that their directions have flipped to avoid crash
        self.assertEqual(self.aquarium.animals[0].directionH, 0)
        self.assertEqual(self.aquarium.animals[1].directionH, 1)

if __name__ == '__main__':
    unittest.main()
