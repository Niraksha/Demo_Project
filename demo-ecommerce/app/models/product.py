# app/models/product.py

class Product:
    def __init__(self, id, name, price, stock, category):
        self.id       = id
        self.name     = name
        self.price    = price
        self.stock    = stock
        self.category = category

    def to_dict(self):
        return {
            "id":       self.id,
            "name":     self.name,
            "price":    self.price,
            "stock":    self.stock,
            "category": self.category
        }

    def is_available(self):
        return self.stock > 0

    def apply_discount(self, percent):
        # intentional bug — no validation on percent value
        self.price = self.price - (self.price * percent / 100)
        return self.price
