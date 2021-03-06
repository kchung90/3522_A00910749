"""
@author Kevin Chung

This module holds information about the 4 budget categories used in the
F.A.M. system.

Each budget category has their own budget limits and hold amount spent
for each budget. Budgets can be locked depending on the amount spent
and the type of the user.
"""
import enum


class Budget:
    """
    Represent a budget of one category for the user.
    """
    def __init__(self, budget_type, total_budget):
        """
        Initialize the budget object
        :param budget_type: budget type as a BudgetType Enum
        :param total_budget: total limit for the budget as a float
        """
        self.budget_type = budget_type
        self.total_budget = total_budget
        self.budget_spent = 0
        self.budget_remaining = total_budget
        self.is_locked = False

    def __str__(self):
        """
        Return the description of the budget object
        :return: the description as a String
        """
        return "%-20s%-20s%-20s%-20s%s" % (f"{self.budget_type.name}",
                                           f"${self.total_budget:.2f}",
                                           f"${self.budget_spent:.2f}",
                                           f"${self.budget_remaining:.2f}",
                                           f"{self.get_lock_status()}")

    def get_lock_status(self):
        """
        Return the status of the budget. Used to find out whether the
        budget is locked or not.
        :return: status of the budget as a String
        """
        if self.is_locked:
            return "Locked"
        return "Unlocked"


class BudgetTypes(enum.Enum):
    """
    Store information about each of 4 budget categories as enumerates.
    """
    GAMES = 1
    CLOTHING = 2
    FOOD = 3
    MISC = 4
