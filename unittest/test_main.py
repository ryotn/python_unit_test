import unittest
from program.main import add_one
from program.main import multiply_by_two
from program.main import my_partial_fn


class TestAddOne(unittest.TestCase):
    def test_add_one_int(self):
        self.assertEqual(add_one(1), 2)
        self.assertEqual(add_one(10), 11)
        self.assertEqual(add_one(11), 12)
        self.assertEqual(add_one(13), 14)

    def test_multiply_by_two(self):
        self.assertEqual(multiply_by_two(2), 4)
        self.assertEqual(multiply_by_two(0), 0)
        self.assertEqual(multiply_by_two(-3), -6)

    def test_add_one_zero(self):
        self.assertEqual(add_one(0), 1)

    def test_add_one_negative(self):
        self.assertEqual(add_one(-2), -1)

    def test_add_one_float(self):
        self.assertAlmostEqual(add_one(1.5), 2.5)

    def test_add_one_type_error(self):
        with self.assertRaises(TypeError):
            add_one("a")

    def test_my_partial_fn(self):
        self.assertEqual(my_partial_fn(1), 10)
        #self.assertEqual(my_partial_fn(0), 0)


if __name__ == "__main__":
    unittest.main()
