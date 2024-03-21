import unittest
from models import BallVector
from utilities import print_result

correct_answer = BallVector(1280, 900)

user_input_close = BallVector(1190, 800)
user_input_far = BallVector(1000, 600)
user_input_equal = BallVector(1280, 900)
user_input_negative = BallVector(-1190, -800)


class TestBallVector(unittest.TestCase):

    def test_subtraction(self):
        vector1 = BallVector(3, 5)
        vector2 = BallVector(1, 2)

        expected_result = BallVector(2, 3)

        self.assertEqual(vector1 - vector2, expected_result)

    def test_result_far(self):
        result = print_result(user_input_far, correct_answer)
        expected_output = 'You need to practice more!'

        self.assertEqual(result, expected_output)

    def test_result_negative(self):
        result = print_result(user_input_negative, correct_answer)
        expected_output = 'Invalid input please enter only positive values'

        self.assertEqual(result, expected_output)

    def test_result_close(self):
        result2 = print_result(user_input_close, correct_answer)
        expected_output2 = 'Ooh! That was close'

        self.assertEqual(result2, expected_output2)

    def test_result_equal(self):
        result3 = print_result(user_input_equal, correct_answer)
        expected_output3 = 'That was spot on!'

        self.assertEqual(result3, expected_output3)


if __name__ == '__main__':
    unittest.main()
