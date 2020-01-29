from Assignments.Assignment1.user import User
from Assignments.Assignment1.bank_account import BankAccount


class Driver:

    def __init__(self):
        pass

    @classmethod
    def register_user(cls):
        input_name = input("Enter the user's name: ")
        input_age = int(input("Enter the user's age: "))
        input_bank_name = input("Enter the user's bank name: ")
        input_account_num = int(input("Enter the user's "
                                      "bank account number: "))
        input_bank_balance = float(input("Enter the user's bank balance: "))

        bank_account = BankAccount(input_bank_name, input_account_num,
                                   input_bank_balance)
        user = User(input_name, input_age, bank_account)

        return user

    @classmethod
    def run(cls):
        print("Please select an option:")
        input_option = int(input("1) Register a new user\n"
                                 "2) Load test users\n"))

        if input_option == 1:
            cls.register_user()
        elif input_option == 2:
            User.load_test_users()


def main():
    driver = Driver()
    driver.run()


if __name__ == '__main__':
    main()
