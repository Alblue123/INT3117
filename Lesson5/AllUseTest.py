import unittest
from main import calculate_price


class MyTestCase(unittest.TestCase):
    def test_valid_all_uses(self):
        self.assertEqual(calculate_price("Cá Mập", 3), "Unknown fish type")
        self.assertEqual(calculate_price("Cá Thu", 4), 60000)
        self.assertEqual(calculate_price("Cá Mập", -1), "Input không hợp lệ")
        self.assertEqual(calculate_price("Cá Thu", 10), 40000)
        self.assertEqual(calculate_price("Cá Trắm Đen", 18), "Mang về cho heo ăn")


if __name__ == '__main__':
    unittest.main()
