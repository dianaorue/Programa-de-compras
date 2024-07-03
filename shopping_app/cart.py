from ownable import set_owner

class Cart:
    def __init__(self, owner):
        set_owner(self, owner)  # Llama al método set_owner para establecer el propietario
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            return  # Manejo de caso donde el saldo no es suficiente

        # Transferencia de saldo de billetera y propiedad de artículos
        for item in self.items:
            item.owner.wallet.deposit(item.price)  # Deposita el precio en la billetera del propietario del artículo
            item.transfer_ownership(self.owner)    # Transfiere la propiedad del artículo al propietario del carrito

        self.empty()  # Vacía el carrito después de la compra

    def empty(self):
        self.items = []

    def __str__(self):
        return f"Cart of {self.owner}: {', '.join(str(item) for item in self.items)}"
