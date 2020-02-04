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

    def view_trans_by_budget(self, category):
        self.bank_account.get_transaction_by_budget(category)

    def view_bank_account_details(self):
        print("-" * 50)
        print("Here are the details of your bank account:\n")
        print("%-25s%s" % ("Account Holder Name:", f"{self.name}"))
        print("%-25s%s" % ("Account Holder Age:", f"{self.age}"))
        self.bank_account.get_bank_account_details()

    def add_bank_account(self):
        """
        Add a bank account object to the user. After the bank account
        object has been added, this method calls a method to add
        budget to the bank account object
        """
        bank_name = input("Enter the user's bank name: ")
        account_num = int(input("Enter the user's "
                                "bank account number: "))
        bank_balance = float(input("Enter the user's bank balance: "))

        self.bank_account = BankAccount(bank_name, account_num, bank_balance)
        self.bank_account.add_budget()

    def view_budgets(self):
        """
        Print all budget details of the user by its category.
        """
        self.bank_account.get_budget_details()

    @abc.abstractmethod
    def record_transaction(self, amount, category, shop_name):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        """
        pass

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
        test_user = Rebel("Test User", 20)
        test_user.bank_account = BankAccount("Scotiabank", "4536000011112222",
                                             500)
        test_user.bank_account.add_test_budgets()

        return test_user


class Angel(User):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._warning_level = 0.9

    def get_warning_level(self):
        return self._warning_level

    def record_transaction(self, amount, budget_type, shop_name):
        self.bank_account.process_transaction(amount, budget_type, shop_name)
        self.overage_notification(budget_type)
        self.warning_notification(budget_type)

    def overage_notification(self, budget_type):
        if self.bank_account.verify_budget_limit(budget_type):
            print("\nYou have exceeded your total budget for this category.")

    def warning_notification(self, budget_type):
        if self.bank_account\
                .verify_warning_level(budget_type, self.get_warning_level()):
            print(f"\nYou have exceeded {self.get_warning_level() * 100:.0f}% "
                  f"of your budget for this category.")


class Troublemaker(User):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._warning_level = 0.75
        self._lock_level = 1.2

    def get_warning_level(self):
        return self._warning_level

    def get_lock_level(self):
        return self._lock_level

    def record_transaction(self, amount, budget_type, shop_name):
        self.bank_account.process_transaction(amount, budget_type, shop_name)
        self.bank_account.lock_budget(self.get_lock_level(), budget_type)
        self.overage_notification(budget_type)
        self.warning_notification(budget_type)

    def overage_notification(self, budget_type):
        if self.bank_account.verify_budget_limit(budget_type):
            print("\nYou have exceeded your total budget for this category.")

    def warning_notification(self, budget_type):
        if self.bank_account\
                .verify_warning_level(budget_type, self.get_warning_level()):
            print(f"\nYou have exceeded {self.get_warning_level() * 100:.0f}% "
                  f"of your budget for this category.")


class Rebel(User):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._warning_level = 0.5
        self._lock_level = 1
        self.num_locks_allowed = 2

    def get_warning_level(self):
        return self._warning_level

    def get_lock_level(self):
        return self._lock_level

    def record_transaction(self, amount, budget_type, shop_name):
        if self.bank_account.get_num_locks() >= self.num_locks_allowed:
            print("\nYour bank account is locked")
        else:
            self.bank_account.process_transaction(amount, budget_type,
                                                  shop_name)
            self.bank_account.lock_budget(self.get_lock_level(), budget_type)
            self.overage_notification(budget_type)
            self.warning_notification(budget_type)

    def overage_notification(self, budget_type):
        if self.bank_account.verify_budget_limit(budget_type):
            print("\nYOU CAN NO LONGER SPEND MONEY FOR THIS CATEGORY!"
                  "\nYOUR MAXIMUM BUDGET FOR THIS CATEGORY HAS BEEN REACHED!")

    def warning_notification(self, budget_type):
        if self.bank_account\
                .verify_warning_level(budget_type, self.get_warning_level()):
            print(f"\nYou have exceeded {self.get_warning_level() * 100:.0f}%"
                  f" of your budget for this category.")
