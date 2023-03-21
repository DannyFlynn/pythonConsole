class Bank():
    def __init__(self, user):
        self.name = user["name"]
        self.pin = user["pin"]
        self.balance = user["balance"]

    def options(self):

        options = int(input(
            "Please select an option \n 1. Deposit \n 2. Withdraw \n 3. Balance \n 4. Return Card: "))
        if options == 1:
            self.bank_deposit()
        elif options == 2:
            self.bank_withdraw()
        elif options == 3:
            self.bank_balance()
        elif options == 4:
            pass
        else:
            self.options()

    def bank_deposit(self):
        deposit = float(
            input("Please insert how much you would like to deposit: "))
        self.balance += deposit
        self.options()

    def bank_withdraw(self):
        withdraw = float(
            input("How much you would like to Withdraw: "))
        if withdraw > self.balance:
            print("Sorry please check your balance as those funds are not available")
            self.options()
        else:
            self.balance -= withdraw
            self.options()

    def bank_balance(self):
        print(f"{self.name} your balance is: {self.balance:.2f}")
        self.options()
