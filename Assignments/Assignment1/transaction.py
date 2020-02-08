"""
@author Kevin Chung

This module depicts a transaction a user makes.

Transactions are validated in the BankAccount class.
"""
from datetime import datetime


class Transaction:
    """
    Represents a transaction a user makes
    """
    def __init__(self, amount, budget_type, shop_name):
        """
        Initialize the transaction object
        :param amount: amount spent as a float
        :param budget_type: category of the budget as a String
        :param shop_name: name of the shop as a String
        """
        self._amount = amount
        self._budget_type = budget_type
        self._shop_name = shop_name
        self._timestamp = datetime.today().replace(microsecond=0)

    @property
    def amount(self):
        """
        Return the amount spent
        :return: amount as a float
        """
        return self._amount

    @property
    def budget_type(self):
        """
        Return the budget type used for the transaction
        :return: budget type as an integer
        """
        return self._budget_type

    @property
    def shop_name(self):
        """
        Return the name of the shop where the transaction was made
        :return: name of the shop as a String
        """
        return self._shop_name

    @property
    def timestamp(self):
        """
        Return the time when the transaction was processed
        :return: timestamp as a Datetime
        """
        return self._timestamp

    def __str__(self):
        """
        Describes the transaction object
        :return: the description of the Transaction object as a String
        """
        return "%-30s%-20s%-20s%s" % (f"{self.timestamp}",
                                      f"${self.amount:.2f}",
                                      f"{self.budget_type}",
                                      f"{self.shop_name}")
