from Assignments.Assignment1.user import User
from Assignments.Assignment1.bank_account import BankAccount
from Assignments.Assignment1.menu import Menu
from Assignments.Assignment1.budget import BudgetTypes
from Assignments.Assignment1.budget import Budget
from Assignments.Assignment1.transaction import Transaction
from datetime import datetime


class Driver:

    def __init__(self):
        self.user = None
        self.menu = None

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
        self.menu = Menu(self.user)

    def run(self):
        print("Please select an option:")
        input_option = int(input("1) Register a new user\n"
                                 "2) Load test users\n"))

        if input_option == 1:
            self.register_user()
        elif input_option == 2:
            User.load_test_users()

        input_menu = int(input("Select the following menu:\n"
                               "1) Record Transaction\n"))

        transaction = None

        if input_menu == 1:
            input_trans_time = (input("Enter the date and time of the "
                                      "transaction in the following format\n"
                                      "(ex. YYYY, MM, DD, HH, MM, SS): "))
            year = int(input_trans_time.split(',')[0].lstrip('0'))
            month = int(input_trans_time.split(',')[1].lstrip('0'))
            day = int(input_trans_time.split(',')[2].lstrip('0'))
            hour = int(input_trans_time.split(',')[3].lstrip('0'))
            minute = int(input_trans_time.split(',')[4].lstrip('0'))
            second = int(input_trans_time.split(',')[5].lstrip('0'))
            trans_time = datetime(year, month, day, hour, minute, second)

            input_trans_amount = float(input("Enter the amount spent: "))
            input_trans_category = int(input(f"Select a category:\n"
                                             f"1) {BudgetTypes(1).name}\n"
                                             f"2) {BudgetTypes(2).name}\n"
                                             f"3) {BudgetTypes(3).name}\n"
                                             f"4) {BudgetTypes(4).name}\n"))
            input_shop_name = input("Enter the name of the shop: ")

            transaction = Transaction(trans_time, input_trans_amount,
                                      input_trans_category, input_shop_name)

        self.menu.record_transaction(transaction)


def main():
    driver = Driver()
    driver.run()


if __name__ == '__main__':
    main()
