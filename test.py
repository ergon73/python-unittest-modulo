import unittest

from main import modulo


class TestModulo(unittest.TestCase):

    def test_modulo_success(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 6), 2)
        self.assertEqual(modulo(15, 5), 0)
        self.assertEqual(modulo(7, 2), 1)
        self.assertEqual(modulo(0, 5), 0)

    def test_modulo_by_zero(self):
        self.assertRaises(ValueError, modulo, 10, 0)
        self.assertRaises(ValueError, modulo, 0, 0)


if __name__ == "__main__":
    unittest.main()
