class CashRegister:
    def __init__(self):
        self._items = []
        self._last_transaction_amount = 0
        self._total = 0

    @property
    def items(self):
        return self._items

    @property
    def total(self):
        return self._total

    def add_item(self, item_cost):
        self._items.append(item_cost)
        self._last_transaction_amount = item_cost
        self._total += item_cost

    def void_last_transaction(self):
        if self._last_transaction_amount != 0:
            self._total -= self._last_transaction_amount
            self._items.pop()
            self._last_transaction_amount = 0

    def apply_discount(self, discount_percentage):
        if discount_percentage > 0 and discount_percentage <= 100:
            discount_amount = (discount_percentage / 100.0) * self._total
            self._total -= discount_amount
            return self._total
        else:
            return "Invalid discount percentage. Discount should be between 0 and 100."

    def clear(self):
        self._items = []
        self._last_transaction_amount = 0
        self._total = 0

