import unittest
from program.main import add_one


class TestAddOne(unittest.TestCase):
    def test_add_one_int(self):
        self.assertEqual(add_one(1), 2)

    def test_add_one_zero(self):
        self.assertEqual(add_one(0), 1)

    def test_add_one_negative(self):
        self.assertEqual(add_one(-2), -1)

    def test_add_one_float(self):
        self.assertAlmostEqual(add_one(1.5), 2.5)

    def test_add_one_type_error(self):
        with self.assertRaises(TypeError):
            add_one("a")


if __name__ == "__main__":
    unittest.main()
