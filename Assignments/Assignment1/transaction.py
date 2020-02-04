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
        self.amount = amount
        self.budget_type = budget_type
        self.shop_name = shop_name
        self.timestamp = datetime.today().replace(microsecond=0)

    def __str__(self):
        """
        Describes the transaction object
        :return: the description of the Transaction object as a String
        """
        return "%-25s%-15s%-15s%s" % (f"{self.timestamp}",
                                      f"{self.amount:.2f}",
                                      f"{self.budget_type}",
                                      f"{self.shop_name}")
