class Item:
    instances = []
from ownable import set_owner

class Item:
    def __init__(self, name, price, owner):
        self.name = name
        self.price = price
        set_owner(self, owner)  # Llama a la función set_owner

    def __str__(self):
        return f"{self.name}({self.price}円)"


    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # instancesを返します ==> Item.item_all()でこれまでに生成されたItemインスタンスを全て返すということです。
        return Item.instances
