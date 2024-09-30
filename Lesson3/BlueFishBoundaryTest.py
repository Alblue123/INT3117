import unittest
from main import calculate_price


class TestFishPricing(unittest.TestCase):
    def test_valid_black_carp(self):
        self.assertEqual(calculate_price("Cá Trắm Đen", 0), 60000)
        self.assertEqual(calculate_price("Cá Trắm Đen", 16), 40000)
        self.assertEqual(calculate_price("Cá Trắm Đen", 8), 60000)
        self.assertEqual(calculate_price("Cá Trắm Đen", 1), 60000)
        self.assertEqual(calculate_price("Cá Trắm Đen", 15), 40000)

    def test_valid_mackerel(self):
        self.assertEqual(calculate_price("Cá Thu", 0), 60000)
        self.assertEqual(calculate_price("Cá Thu", 16), 40000)
        self.assertEqual(calculate_price("Cá Thu", 8), 60000)
        self.assertEqual(calculate_price("Cá Thu", 1), 60000)
        self.assertEqual(calculate_price("Cá Thu", 15), 40000)


if __name__ == '__main__':
    unittest.main()
