class Money:

    def insert_money(self):
        inserted = False
        while inserted == False:

            payed = int(input("Please insert money its  one pound per turn, machine only accepts pounds: "))
            if payed >= 1:
                inserted = True
                return payed