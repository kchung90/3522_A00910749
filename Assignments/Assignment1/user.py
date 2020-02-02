"""
@author Kevin Chung

This module depicts a user who participates in the F.A.M. program.

A user initially has a name and an age. Bank account information are to
be added to the user.
"""
import abc
from Assignments.Assignment1.bank_account import BankAccount
from Assignments.Assignment1.budget import Budget
from Assignments.Assignment1.budget import BudgetTypes


class User:
    """
    Represents a user object who participate in this program.
    """
    def __init__(self, name, age):
        """
        Initialize a user by taking in the name and the age. Bank
        account information are set to None at the beginning.
        :param name: name of the user as a String
        :param age: age of the user as an integer
        """
        self.name = name
        self.age = age
        self.bank_account = None

    def view_budgets(self):
        """
        Print all budget details of the user by its category.
        """
        self.bank_account.get_budget_details()

    def record_transaction(self):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        """
        self.bank_account.process_transaction()

    def view_transactions_by_budget(self):
        pass

    def add_bank_account(self):
        """
        Add a bank account object to the user. After the bank account
        object has been added, this method calls a method to add
        budget to the bank account object
        """
        input_bank_name = input("Enter the user's bank name: ")
        input_account_num = int(input("Enter the user's "
                                      "bank account number: "))
        input_bank_balance = float(input("Enter the user's bank balance: "))

        self.bank_account = BankAccount(input_bank_name, input_account_num,
                                        input_bank_balance)
        self.bank_account.add_budget()

    @classmethod
    def load_test_user(cls):
        """
        Initialize a test user by hardcoding the information for a
        testing purpose.
        A test user has all the information including the bank account
        and budget information.
        :return: a test user as a User object
        """
        test_user = User("Test User", 20)

        test_user.bank_account = BankAccount("Scotiabank", "4536000011112222",
                                             500)

        test_budget_1 = Budget(BudgetTypes(1).name, 100)
        test_budget_2 = Budget(BudgetTypes(2).name, 100)
        test_budget_3 = Budget(BudgetTypes(3).name, 200)
        test_budget_4 = Budget(BudgetTypes(4).name, 100)

        test_user.bank_account.budgets.append(test_budget_1)
        test_user.bank_account.budgets.append(test_budget_2)
        test_user.bank_account.budgets.append(test_budget_3)
        test_user.bank_account.budgets.append(test_budget_4)

        return test_user
