import unittest
from montyhall import MontyHall

class MontyHallTest(unittest.TestCase):

    def test_make_choice(self):
        num_doors      = 3
        num_rounds     = 1000
        one_third      = float(1) / 3
        two_thirds     = float(2) / 3
        accepted_delta = 0.05

        correct_guesses_initial = [MontyHall(num_doors).make_choice(keep_initial_choice=True) for i in range(num_rounds)].count(True)
        correct_guesses_changed = [MontyHall(num_doors).make_choice(keep_initial_choice=False) for i in range(num_rounds)].count(True)

        # Keeping initial guess should give us 1/3 correct correct guesses
        self.assertAlmostEqual(correct_guesses_initial, one_third * num_rounds, delta=accepted_delta * num_rounds)
        # Changing initial guess should give us 2/3 correct correct guesses
        self.assertAlmostEqual(correct_guesses_changed, two_thirds * num_rounds, delta=accepted_delta * num_rounds)

if __name__ == '__main__':
    unittest.main()
    