"""
@author Kevin Chung

This module depicts a user who participates in the F.A.M. program.

User class is an abstract class and three user types (Angel,
Troublemaker, and Rebel) inherit from the User class.

A user initially has a name and an age. Bank account information are to
be added to the user.
"""
import abc
from Assignments.Assignment1.bank_account import BankAccount


class User(abc.ABC):
    """
    An abstract class which represents a user object who participates
    in the F.A.M. program.
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
        self._bank_account = None

    @property
    def bank_account(self):
        """
        Return bank account object of the user
        :return: bank account as a BankAccount object
        """
        return self._bank_account

    def view_trans_by_budget(self, budget_type):
        """
        Let the user view all processed transactions up to date by each
        budget type
        :param budget_type: budget_type as an integer
        """
        self.bank_account.get_transaction_by_budget(budget_type)

    def view_bank_account_details(self):
        """
        Let the user view all details of his bank account including
        the account holder's name and age, name of the bank, account
        number, current balance remaining, and all transactions
        processed up to date.
        """
        print("\n" + "-" * 100)
        print("Your Bank Account Details")
        print("-" * 100)

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

        self._bank_account = BankAccount(bank_name, account_num, bank_balance)
        self.bank_account.add_budget()

    def view_budgets(self):
        """
        Print all budget details of the user by its category.
        """
        self.bank_account.get_budget_details()

    @abc.abstractmethod
    def record_transaction(self, amount, budget_type, shop_name):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        Needs to be overridden by each child class.
        """
        pass

    @abc.abstractmethod
    def overage_notification(self, budget_type):
        """
        Sends out a notification to the user when the user spends more
        than the budget limit.
        Needs to be overridden by each child class.
        :param budget_type: budget type as an integer
        """
        pass

    @abc.abstractmethod
    def warning_notification(self, budget_type):
        """
        Sends out a notification to the user when the user spends more
        than certain percentage of its budget for each type. The
        percentage level differs by its user type.
        Needs to be overridden by each child class.
        :param budget_type: budget type as an integer
        """
        pass

    @classmethod
    def load_test_user(cls):
        """
        Initialize a test user by hard-coding the information for a
        testing purpose.
        A test user has all the information including the bank account
        and budget information.
        :return: a test user as a User object
        """
        test_user = Rebel("Test User", 20)
        test_user._bank_account = BankAccount("Scotiabank", "4536000011112222",
                                              500)
        test_user.bank_account.add_test_budgets()

        return test_user


class Angel(User):
    """
    Represent an Angel type user.

    Angel type users never get locked out of a budget category. As long
    as they have a balance in their bank account, they can continue
    spending money

    They get notified when they exceed 90% and 100% of their budget.
    """

    def __init__(self, name, age):
        """
        Initiate an Angel Type object
        :param name: name of the user as a String
        :param age: age of the user as an integer
        """
        super().__init__(name, age)
        self._warning_level = 0.9

    @property
    def warning_level(self):
        """
        Return the warning level of the Angel type user
        :return: warning level as a float
        """
        return self._warning_level

    def record_transaction(self, amount, budget_type, shop_name):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        When transactions are recorded, notifications are sent out
        depending on the amount the user has spent for each category.
        :param amount: amount to spend as a float
        :param budget_type: budget type as an integer
        :param shop_name: name of the shop as a String
        """
        if self.bank_account.verify_transaction(amount, budget_type):
            self.bank_account.process_transaction(amount, budget_type,
                                                  shop_name)
            self.overage_notification(budget_type)
            self.warning_notification(budget_type)

    def overage_notification(self, budget_type):
        """
        Print out a notification to the user when the user exceeds the
        budget limit.
        :param budget_type: budget type as an integer
        """
        if self.bank_account.verify_budget_limit(budget_type):
            print("\n[IMPORTANT]"
                  "\nYou have exceeded your total budget for this category.")

    def warning_notification(self, budget_type):
        """
        Print out a notification to the user when the user spends more
        than the warning level.
        Warning level for Angel type user is set to 90%
        :param budget_type: budget type as an integer
        """
        if self.bank_account\
                .verify_warning_level(budget_type, self.warning_level):
            print(f"\n[WARNING]\n"
                  f"You have exceeded {self.warning_level * 100:.0f}% "
                  f"of your budget for this category.")


class Troublemaker(User):
    """
    Represent a Troublemaker type user

    Troublemaker user types get locked out of a budget category if they
    exceed 120% of their budget.

    They get notified when they exceed 75% and 100% of their budget.
    """

    def __init__(self, name, age):
        """
        Initialize Troublemaker user type
        :param name: name of the user as a String
        :param age: age of the user as an integer
        """
        super().__init__(name, age)
        self._warning_level = 0.75
        self._lock_level = 1.2

    @property
    def warning_level(self):
        """
        Return the warning level of the Troublemaker type user
        :return: warning level as a float
        """
        return self._warning_level

    @property
    def lock_level(self):
        """
        Return the lock out level of the Troublemaker type user
        :return: lock out level as a float
        """
        return self._lock_level

    def record_transaction(self, amount, budget_type, shop_name):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        When transactions are recorded, notifications are sent out
        depending on the amount the user has spent for each category.
        Also, when the amount spent for a budget exceed the lock out
        level, the budget category will be locked.
        :param amount: amount to spend as a float
        :param budget_type: budget type as an integer
        :param shop_name: name of the shop as a String
        """
        if self.bank_account.verify_transaction(amount, budget_type):
            self.bank_account.process_transaction(amount, budget_type,
                                                  shop_name)
            self.overage_notification(budget_type)
            self.warning_notification(budget_type)
            self.bank_account.lock_budget(self.lock_level, budget_type)

    def overage_notification(self, budget_type):
        """
        Print out a notification to the user when the user exceeds the
        budget limit.
        :param budget_type: budget type as an integer
        :return:
        """
        if self.bank_account.verify_budget_limit(budget_type):
            print("\n[IMPORTANT]"
                  "\nYou have exceeded your total budget for this category.")

    def warning_notification(self, budget_type):
        """
        Print out a notification to the user when the user spends more
        than the warning level.
        Warning level for Angel type user is set to 90%
        :param budget_type: budget type as an integer
        """
        if self.bank_account\
                .verify_warning_level(budget_type, self.warning_level):
            print(f"\n[WARNING]\n"
                  f"You have exceeded {self.warning_level * 100:.0f}% "
                  f"of your budget for this category.")


class Rebel(User):
    """
    Represent a Rebel type user

    Rebel type user gets locked out of a budget category when they
    exceed 100% of their budget.
    When they are locked out from 2 or more categories, they get locked
    out of their bank account and can no longer make transactions.

    They get notified when they exceed 50% and 100% of their budget.
    """

    def __init__(self, name, age):
        """
        Initialize the Rebel type user
        :param name: name of the user as a String
        :param age: age of the user as an integer
        """
        super().__init__(name, age)
        self._warning_level = 0.5
        self._lock_level = 1
        self.num_locks_allowed = 2

    @property
    def warning_level(self):
        """
        Return the warning level of the Rebel type user
        :return: warning level as a float
        """
        return self._warning_level

    @property
    def lock_level(self):
        """
        Return the lock out level of the Rebel type user
        :return: lock out level as a float
        """
        return self._lock_level

    def record_transaction(self, amount, budget_type, shop_name):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        When transactions are recorded, notifications are sent out
        depending on the amount the user has spent for each category.
        Also, when the amount spent for a budget exceed the lock out
        level, the budget category will be locked.
        If 2 or more budget categories are locked, user gets locked out
        from their bank account.
        :param amount: amount to spend as a float
        :param budget_type: budget type as an integer
        :param shop_name: name of the shop as a String
        """
        if self.bank_account.num_locked >= self.num_locks_allowed:
            print("\n[CRITICAL]"
                  "\nYOUR BANK ACCOUNT HAS BEEN LOCKED."
                  "\nYOU CAN NO LONGER MAKE ANY TRANSACTIONS.")
        else:
            if self.bank_account.verify_transaction(amount, budget_type):
                self.bank_account.process_transaction(amount, budget_type,
                                                      shop_name)
                self.overage_notification(budget_type)
                self.warning_notification(budget_type)
                self.bank_account.lock_budget(self.lock_level, budget_type)

    def overage_notification(self, budget_type):
        """
        Print out a notification to the user when the user exceeds the
        budget limit.
        :param budget_type: budget type as an integer
        """
        if self.bank_account.verify_budget_limit(budget_type):
            print("\n[IMPORTANT]"
                  "\nYOU HAVE EXCEEDED YOUR TOTAL BUDGET FOR THIS "
                  "CATEGORY!!!")

    def warning_notification(self, budget_type):
        """
        Print out a notification to the user when the user spends more
        than the warning level.
        :param budget_type: budget type as an integer
        """
        if self.bank_account\
                .verify_warning_level(budget_type, self.warning_level):
            print(f"\n[WARNING]\n"
                  f"You have exceeded {self.warning_level * 100:.0f}%"
                  f" of your budget for this category.")
