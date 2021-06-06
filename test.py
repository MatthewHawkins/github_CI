import unittest
import example


class Testcase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.addition(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(1, 0), 1)

    def test_mult_1(self):
        self.assertEqual(example.multiply(1, 0), 0)

    def test_div_1(self):
        self.assertEqual(example.divide(1, 1), 1)


if __name__ == '__main__':
    unittest.main()
