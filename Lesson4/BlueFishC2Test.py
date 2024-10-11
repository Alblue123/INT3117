import unittest
from main import calculate_price


class TestFishPricing(unittest.TestCase):
    def test_valid_C2(self):
        self.assertEqual(calculate_price("Cá Thu", -3), "Input không hợp lệ")
        self.assertEqual(calculate_price("Cá Mập", 10), "Unknown fish type")
        self.assertEqual(calculate_price("Cá Thu", 3), 60000)
        self.assertEqual(calculate_price("Cá Thu", 12), 40000)
        self.assertEqual(calculate_price("Cá Trắm Đen", 19), "Mang về cho heo ăn")


if __name__ == '__main__':
    unittest.main()
