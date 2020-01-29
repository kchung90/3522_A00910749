from Assignments.Assignment1.user import User
from Assignments.Assignment1.bank_account import BankAccount
from Assignments.Assignment1.menu import Menu
from Assignments.Assignment1.budget import BudgetTypes
from Assignments.Assignment1.budget import Budget


class Driver:

    def __init__(self):
        self.user = None
        self.menu = Menu()

    def register_user(self):
        input_name = input("Enter the user's name: ")
        input_age = int(input("Enter the user's age: "))
        input_bank_name = input("Enter the user's bank name: ")
        input_account_num = int(input("Enter the user's "
                                      "bank account number: "))
        input_bank_balance = float(input("Enter the user's bank balance: "))

        budgets = []

        for i in BudgetTypes:
            input_total_budget = float(input(f"Enter the total budget for "
                                             f"'{BudgetTypes(i).name}' "
                                             f"category: "))
            budgets.append(Budget(BudgetTypes(i).name, input_total_budget))

        bank_account = BankAccount(input_bank_name, input_account_num,
                                   input_bank_balance, budgets)
        self.user = User(input_name, input_age, bank_account)

    def run(self):
        print("Please select an option:")
        input_option = int(input("1) Register a new user\n"
                                 "2) Load test users\n"))

        if input_option == 1:
            self.register_user()
        elif input_option == 2:
            User.load_test_users()


def main():
    driver = Driver()
    driver.run()


if __name__ == '__main__':
    main()
