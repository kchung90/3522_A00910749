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
    def __init__(self, amount, budget_category, shop_name):
        """
        Initialize the transaction object
        :param amount: amount spent as a float
        :param budget_category: category of the budget as a String
        :param shop_name: name of the shop as a String
        """
        self.amount = amount
        self.budget_category = budget_category
        self.shop_name = shop_name
        self.timestamp = datetime.today().replace(microsecond=0)

    def __str__(self):
        """
        Describes the transaction object
        :return: the description of the Transaction object as a String
        """
        return "%-25s%-15s%-15s%s" % (f"{self.timestamp}",
                                      f"{self.amount:.2f}",
                                      f"{self.budget_category}",
                                      f"{self.shop_name}")
