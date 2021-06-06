import unittest
import example


class Testcase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.addition(1, 2), 3)
    def test_add_1(self):
        self.assertEqual(example.subtraction(1, 0), 1)


if __name__ == '__main__':
    unittest.main()
