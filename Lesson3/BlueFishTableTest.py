import unittest
from main import calculate_price


class TestFishPricing(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual(calculate_price("Cá Trắm Đen", -1), "Input không hợp lệ")
        self.assertEqual(calculate_price("Cá Thu", -5), "Input không hợp lệ")

    def test_valid_black_carp(self):
        self.assertEqual(calculate_price("Cá Trắm Đen", 5), 60000)
        self.assertEqual(calculate_price("Cá Trắm Đen", 10), 40000)

    def test_valid_mackerel(self):
        self.assertEqual(calculate_price("Cá Thu", 2), 60000)
        self.assertEqual(calculate_price("Cá Thu", 12), 40000)

    def test_fish_too_old(self):
        self.assertEqual(calculate_price("Cá Trắm Đen", 17), "Mang về cho heo ăn")
        self.assertEqual(calculate_price("Cá Thu", 18), "Mang về cho heo ăn")


if __name__ == '__main__':
    unittest.main()
