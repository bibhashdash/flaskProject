import unittest
from app import BallVector


class TestBallVector(unittest.TestCase):

    def test_subtraction(self):
        vector1 = BallVector(3, 5)
        vector2 = BallVector(1, 2)

        expected_result = BallVector(2, 3)

        self.assertEqual(vector1 - vector2, expected_result)


if __name__ == '__main__':
    unittest.main()
