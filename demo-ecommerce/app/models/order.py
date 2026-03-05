# app/models/order.py
from datetime import datetime

class Order:
    def __init__(self, id, user_id, items):
        self.id         = id
        self.user_id    = user_id
        self.items      = items   # list of {"product_id": x, "quantity": y}
        self.status     = "pending"
        self.created_at = datetime.now()
        self.total      = 0

    def calculate_total(self, products):
        # intentional bug — no check if product exists in list
        total = 0
        for item in self.items:
            product = products[item["product_id"]]
            total += product.price * item["quantity"]
        self.total = total
        return total

    def to_dict(self):
        return {
            "id":         self.id,
            "user_id":    self.user_id,
            "items":      self.items,
            "status":     self.status,
            "total":      self.total,
            "created_at": str(self.created_at)
        }
