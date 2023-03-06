import unittest
from add import StringCalculator


class TestAdd(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(StringCalculator().add(""), 0)

    def test_one(self):
        self.assertEqual(StringCalculator().add("1"), 1)

    def test_add_multiple(self):
        self.assertEqual(StringCalculator().add("1,2,434"), 437)

    def test_negative_add(self):
        with self.assertRaises(Exception):
            StringCalculator().add("-1,2,434")

    def test_ignore_over_1000(self):
        self.assertEqual(StringCalculator().add("1,2,434,1001"), 437)


if __name__ == "__main__":
    unittest.main()
