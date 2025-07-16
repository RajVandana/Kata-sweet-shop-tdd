# tests/test_shop.py

import unittest
from sweetshop.models import Sweet
from sweetshop.shop import SweetShop

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        self.shop = SweetShop()
        self.sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.sweet2 = Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        self.shop.add_sweet(self.sweet1)
        self.shop.add_sweet(self.sweet2)

    def test_add_sweet(self):
        sweet3 = Sweet(1003, "Gulab Jamun", "Milk-Based", 40, 25)
        self.shop.add_sweet(sweet3)
        self.assertEqual(len(self.shop.sweets), 3)

    def test_add_duplicate_sweet(self):
        with self.assertRaises(ValueError):
            self.shop.add_sweet(self.sweet1)

    def test_delete_sweet(self):
        self.shop.delete_sweet(1001)
        self.assertEqual(len(self.shop.sweets), 1)

    def test_view_sweets(self):
        sweets = self.shop.view_sweets()
        self.assertEqual(len(sweets), 2)

    def test_search_by_name(self):
        result = self.shop.search_by_name("Halwa")
        self.assertEqual(result[0].name, "Gajar Halwa")

    def test_search_by_category(self):
        result = self.shop.search_by_category("Nut-Based")
        self.assertEqual(result[0].name, "Kaju Katli")

    def test_search_by_price_range(self):
        result = self.shop.search_by_price_range(25, 35)
        self.assertEqual(result[0].name, "Gajar Halwa")

    def test_sort_by_price(self):
        result = self.shop.sort_by_price()
        self.assertEqual(result[0].name, "Gajar Halwa")

    def test_sort_by_name(self):
        result = self.shop.sort_by_name()
        self.assertEqual(result[0].name, "Gajar Halwa")

    def test_purchase_sweet(self):
        self.shop.purchase_sweet(1001, 5)
        self.assertEqual(self.sweet1.quantity, 15)

    def test_purchase_sweet_insufficient_stock(self):
        with self.assertRaises(ValueError):
            self.shop.purchase_sweet(1002, 100)

    def test_restock_sweet(self):
        self.shop.restock_sweet(1002, 10)
        self.assertEqual(self.sweet2.quantity, 25)

if __name__ == "__main__":
    unittest.main()
