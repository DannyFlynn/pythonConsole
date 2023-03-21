from data import bank_details
from create_account import CreateAccount
from validation import Validation
from bank import Bank


def start_menu():
    start = int(input(
        "Welcome for new accounts please type (9) otherwise any other key to continue: "))
    if start == 9:
        account_creation()
    else:
        validate_pin()


def account_creation():
    name = input("\nPlease enter your name: ")
    new_account = CreateAccount(name)
    new_account.create(bank_details)
    print("please keep your pin safe \n")
    start_menu()


def validate_pin():
    logged_out = True
    attempts = 3
    while logged_out:
        print(f"You have {attempts} attempts left.")
        pin = int(input(
            "please enter your pin: "))
        logged_in = Validation(pin, bank_details)
        user = logged_in.match()

        if user == False:
            print("incorrect")
            attempts -= 1
        else:
            print(user["name"])
            main_menu(user)
            logged_out = False


def main_menu(user):
    print("Hello ", user["name"])
    customer = Bank(user)
    customer_choice = customer.options()
    print(f"Thank {user['name']} for using our bank have a lovely day.")
    start_menu()


start_menu()
