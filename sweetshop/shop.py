# sweetshop/shop.py

from sweetshop.models import Sweet

class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        if any(s.id == sweet.id for s in self.sweets):
            raise ValueError("Sweet with this ID already exists.")
        self.sweets.append(sweet)

    def delete_sweet(self, sweet_id):
        self.sweets = [s for s in self.sweets if s.id != sweet_id]

    def view_sweets(self):
        return self.sweets

    def search_by_name(self, name):
        return [s for s in self.sweets if name.lower() in s.name.lower()]

    def search_by_category(self, category):
        return [s for s in self.sweets if s.category.lower() == category.lower()]

    def search_by_price_range(self, min_price, max_price):
        return [s for s in self.sweets if min_price <= s.price <= max_price]

    def sort_by_price(self):
        return sorted(self.sweets, key=lambda s: s.price)

    def sort_by_name(self):
        return sorted(self.sweets, key=lambda s: s.name.lower())

    def purchase_sweet(self, sweet_id, quantity):
        for s in self.sweets:
            if s.id == sweet_id:
                if s.quantity >= quantity:
                    s.quantity -= quantity
                    return
                else:
                    raise ValueError("Not enough stock available.")
        raise ValueError("Sweet not found.")

    def restock_sweet(self, sweet_id, quantity):
        for s in self.sweets:
            if s.id == sweet_id:
                s.quantity += quantity
                return
        raise ValueError("Sweet not found.")
