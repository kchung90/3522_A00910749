"""
@author Kevin Chung

This module depicts a user who participates in the F.A.M. program.

A user initially has a name and an age. Bank account information are to
be added to the user.
"""
import abc
from Assignments.Assignment1.bank_account import BankAccount


class User(abc.ABC):
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

    @abc.abstractmethod
    def record_transaction(self, amount, category, shop_name):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        """
        pass

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

    def add_test_bank_account(self):
        self.bank_account = BankAccount("Scotiabank", "4536000011112222",
                                        500)

    def view_budgets(self):
        """
        Print all budget details of the user by its category.
        """
        self.bank_account.get_budget_details()

    @abc.abstractmethod
    def overage_notification(self, category):
        pass

    @abc.abstractmethod
    def warning_notification(self, category):
        pass

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
        test_user.bank_account.add_test_bank_account()
        test_user.bank_account.add_test_budgets()

        return test_user
