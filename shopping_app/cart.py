from ownable import set_owner
from collections import defaultdict

class Cart:
    def __init__(self, owner):
        set_owner(self, owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item, quantity=1):
        self.items.append({"item": item, "quantity": quantity})

    def total_amount(self):
        price_list = [entry["item"].price * entry["quantity"] for entry in self.items]
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            return

        for entry in self.items:
            item = entry["item"]
            item.owner.wallet.deposit(item.price * entry["quantity"])
            item.transfer_ownership(self.owner)

        self.empty()

    def empty(self):
        self.items = []

    def show_items(self):
        if not self.items:
            print("🛒 カートは空です")
        else:
            print("🛒 Contents of cart")
            print("+----+--------------+--------+----------+")
            print("| No.| Product Name | Amount | Quantity |")
            print("+====+==============+========+==========+")

            item_summary = defaultdict(lambda: {"price": 0, "quantity": 0})
            for entry in self.items:
                item = entry["item"]
                item_summary[item.name]["price"] = item.price
                item_summary[item.name]["quantity"] += entry["quantity"]

            for index, (name, details) in enumerate(item_summary.items()):
                print(f"| {index + 1:<2} | {name:<12} | {details['price']:<6} | {details['quantity']:<8} |")
                print("+----+--------------+--------+----------+")

    def __str__(self):
        return f"Cart of {self.owner}: {', '.join(str(entry['item']) for entry in self.items)}"
