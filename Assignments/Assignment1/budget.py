"""
@author Kevin Chung

This module holds information about the 4 budget categories used in the
F.A.M. system.

Each budget category has their own budget limits.
"""
import enum


class Budget:
    """
    Represent a budget of one category for the user.
    """
    def __init__(self, budget_type, total_budget):
        """
        Initialize the budget object
        :param budget_type: category of the budget as a String
        :param total_budget: total limit for the budget as a float
        """
        self.budget_type = budget_type
        self.total_budget = total_budget

    def __str__(self):
        """
        Return the description of the budget object
        :return: the description as a String
        """
        return "%-20s%s" % (f"{self.budget_type}", f"{self.total_budget}")


class BudgetTypes(enum.Enum):
    """
    Store information about each of 4 budget categories as enumerates.
    """
    GAMES = 1
    CLOTHING = 2
    FOOD = 3
    MISC = 4
