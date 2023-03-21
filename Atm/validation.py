class Validation():

    def __init__(self, pin, bank_db):
        self.pin = pin
        self.bank_db = bank_db
        self.success = False

    def match(self):
        # for account in self.bank_db:
        #     if self.pin == account["pin"]:
        #         return account
        # else:
        #     return False
        for account in self.bank_db:
            if self.pin == account["pin"]:

                return {"name": account["name"], "pin": account["pin"], "balance": account["balance"]
                        }
        else:

            return False
