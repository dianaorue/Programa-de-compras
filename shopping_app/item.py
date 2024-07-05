from ownable import set_owner

class Item:
    instances = []

    def __init__(self, name, price, owner):
        self.name = name
        self.price = price
        set_owner(self, owner)
        Item.instances.append(self)  
        

    def transfer_ownership(self, new_owner):
        set_owner(self, new_owner)

    def __str__(self):
        return f"{self.name} ({self.price}円)"

    @staticmethod
    def item_all():
        return Item.instances
