from ownable import set_owner

class Wallet:

    def __init__(self, owner):
        set_owner(self, owner)  # Llama a la función set_owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount
