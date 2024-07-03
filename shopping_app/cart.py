from ownable import set_owner

class Cart:
    def __init__(self, owner):
        set_owner(self, owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = [item.price for item in self.items]
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            return  

        for item in self.items:
            item.owner.wallet.deposit(item.price)
            item.transfer_ownership(self.owner)

        self.empty()  

    def empty(self):
        self.items = []

    def show_items(self):
        if not self.items:
            print("🛒 カートは空です")
        else:
            print("🛒 カートの中身")
            for index, item in enumerate(self.items):
                print(f"{index + 1}. {item}")

    def __str__(self):
        return f"Cart of {self.owner}: {', '.join(str(item) for item in self.items)}"
