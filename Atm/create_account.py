import random


class CreateAccount():
    def __init__(self, name):
        self.name = name
        self.pin = random.randint(1000, 9999)

    def create(self, bank_details):

        print(f"\nThank you {self.name} your pin is {self.pin}")
        new_account = {"name": self.name, "pin": self.pin, "balance": 0}
        bank_details.append(new_account)
