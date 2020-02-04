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

    def __init__(self, name, account_num, balance):
        """
        Initialize a bank account object
        :param name: name of the bank as a String
        :param account_num: account number as an integer
        :param balance: balance as a float
        """
        self.name = name
        self.account_num = account_num
        self._balance = balance
        self.budgets = []
        self.trans_list = {BudgetTypes(1).name: [],
                           BudgetTypes(2).name: [],
                           BudgetTypes(3).name: [],
                           BudgetTypes(4).name: []}
        self.num_locked = 0

    @property
    def get_balance(self):
        """
        Return the balance of the bank account
        :return: balance as a float
        """
        return self._balance

    def get_bank_account_details(self):
        print("%-25s%s" % ("Bank Name:", f"{self.name}"))
        print("%-25s%s" % ("Account Number:", f"{self.account_num}"))
        print("%-25s$%s" % ("Current Balance:", f"{self._balance:.2f}"))

        for i in BudgetTypes:
            self.get_transaction_by_budget(i)

        print("-" * 50)

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

    def get_transaction_by_budget(self, category):
        budget_type = BudgetTypes(category).name
        print(f"\nTransaction Details for {budget_type}:")

        if self.trans_list[f"{budget_type}"]:
            print("%-25s%-15s%-15s%s" % ("Timestamp", "Amount",
                                         "Category", "Shop Name"))
            for transaction in self.trans_list[f"{budget_type}"]:
                print(transaction)
        else:
            print("No Transactions")

    def process_transaction(self, amount, category, shop_name):
        """
        Process transactions that are verified and store the processed
        transaction objects as a list in the dictionary in the bank
        account object. When transactions are processed, the balance in
        the bank account and the budget amount get decreased by the
        amount spent.
        """
        trans_category = BudgetTypes(category).name

        if self.verify_transaction(amount, category):
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

    def verify_transaction(self, amount, budget_type):
        """
        Verify transaction by making sure that the amount spent is less
        than the balance in the user's bank account and return Bool
        depending on the condition
        :param amount: amount spent as a float
        :param budget_type: index of the budget type in the budgets list
        as an integer
        :return: True if the amount spent is less than the balance in
        the user's bank account
        """
        budget = self.budgets[budget_type - 1]
        if amount > self.get_balance:
            return False
        if budget.is_locked:
            return False
        return True

    def lock_budget(self, limit, budget_type):
        budget = self.budgets[budget_type - 1]
        if budget.budget_remaining <= 0 and budget.budget_spent >= \
                budget.total_budget * limit and not budget.is_locked:
            budget.is_locked = True
            self.num_locked = self.num_locked + 1
            print(f"\nBudget is locked for {budget.budget_type}")

    def get_num_locks(self):
        return self.num_locked

    def verify_budget_limit(self, budget_type):
        budget = self.budgets[budget_type - 1]
        if budget.budget_remaining <= 0:
            return True
        return False

    def verify_warning_level(self, budget_type, level):
        budget = self.budgets[budget_type - 1]
        warning_level = budget.total_budget - (budget.total_budget * level)
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
