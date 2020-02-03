"""
@author Kevin Chung

This module depicts the bank account which holds all the banking
information of the user.

Bank account information are used to process valid transactions.
"""
from Assignments.Assignment1.budget import BudgetTypes, Budget
from Assignments.Assignment1.transaction import Transaction


class BankAccount:
    """
    Represents a bank account.
    """

    def __init__(self, name, account_number, balance):
        """
        Initialize a bank account object
        :param name: name of the bank as a String
        :param account_number: account number as an integer
        :param balance: balance as a float
        """
        self.name = name
        self.account_number = account_number
        self._balance = balance
        self.budgets = []
        self.trans_list = {BudgetTypes(1).name: [],
                           BudgetTypes(2).name: [],
                           BudgetTypes(3).name: [],
                           BudgetTypes(4).name: []}

    @property
    def balance(self):
        """
        Return the balance of the bank account
        :return: balance as a float
        """
        return self._balance

    def add_budget(self):
        """
        Create budget objects for each budget category and store the
        budget objects in a list in the bank account object
        """
        for i in BudgetTypes:
            input_total_budget = float(input(f"Enter the total budget for "
                                             f"'{BudgetTypes(i).name}' "
                                             f"category: "))
            self.budgets.append(Budget(BudgetTypes(i).name,
                                       input_total_budget))

    def get_budget_details(self):
        """
        Print the details of each budget by its category
        """
        print("\n%-20s%-20s%-20s%-20s%s" % ("Budget Category",
                                            "Total Budget",
                                            "Budget Spent",
                                            "Budget Remaining",
                                            "Status"))
        for budget in self.budgets:
            print(budget)

    def process_transaction(self, amount, category, shop_name):
        """
        Process transactions that are verified and store the processed
        transaction objects as a list in the dictionary in the bank
        account object. When transactions are processed, the balance in
        the bank account and the budget amount get decreased by the
        amount spent.
        """
        trans_category = BudgetTypes(category).name

        if self.verify_transaction(amount):
            transaction = Transaction(amount,
                                      trans_category, shop_name)

            self._balance = self._balance - transaction.amount

            for budget in self.budgets:
                if budget.budget_type == trans_category:
                    budget.budget_spent = \
                        budget.budget_spent + transaction.amount
                    budget.budget_remaining = \
                        budget.budget_remaining - amount

            self.trans_list[f"{trans_category}"] \
                .append(transaction)

            print("\n%-25s%-15s%-15s%s" % ("Timestamp", "Amount",
                                           "Category", "Shop Name"))
            for transaction in self.trans_list[f"{trans_category}"]:
                print(transaction)
        else:
            print("\nTransaction cannot be processed. You cannot spend more "
                  "than what you have!")

    def verify_transaction(self, amount):
        """
        Verify transaction by making sure that the amount spent is less
        than the balance in the user's bank account and return Bool
        depending on the condition
        :param amount: amount spent as a float
        :return: True if the amount spent is less than the balance in
        the user's bank account
        """
        if amount > self.balance:
            return False
        return True

    def lock_budget(self, limit):
        for budget in self.budgets:
            if budget.budget_remaining < 0 and budget.budget_spent > \
                    budget.total_budget * limit:
                budget.is_locked = True

    def verify_budget_limit(self, category):
        budget_category = BudgetTypes(category).name
        for budget in self.budgets:
            if budget.budget_type == budget_category:
                if budget.budget_remaining < 0:
                    return True
        return False

    def verify_warning_level(self, category, level):
        budget_category = BudgetTypes(category).name
        for budget in self.budgets:
            if budget.budget_type == budget_category:
                warning_level = \
                    budget.total_budget - (budget.total_budget * level)
                if warning_level >= budget.budget_remaining > 0:
                    return True
        return False

    def add_test_budgets(self):
        test_budget_1 = Budget(BudgetTypes(1).name, 100)
        test_budget_2 = Budget(BudgetTypes(2).name, 100)
        test_budget_3 = Budget(BudgetTypes(3).name, 100)
        test_budget_4 = Budget(BudgetTypes(4).name, 100)

        self.budgets.append(test_budget_1)
        self.budgets.append(test_budget_2)
        self.budgets.append(test_budget_3)
        self.budgets.append(test_budget_4)
