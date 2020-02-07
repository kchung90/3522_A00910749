"""
@author Kevin Chung

This module depicts the bank account which holds all the banking
information of a user.

Bank account information are used to process valid transactions.
"""
from Assignments.Assignment1.budget import BudgetTypes, Budget
from Assignments.Assignment1.transaction import Transaction


class BankAccount:
    """
    Represents a bank account object which holds banking information
    and budget information for each category.
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
    def balance(self):
        """
        Return the balance of the bank account
        :return: balance as a float
        """
        return self._balance

    def get_bank_account_details(self):
        """
        Print out all the bank account details including the bank name,
        account number, current balance, and all transactions processed
        for each budget category.
        """
        print("%-25s%s" % ("Bank Name:", f"{self.name}"))
        print("%-25s%s" % ("Account Number:", f"{self.account_num}"))
        print("%-25s$%s" % ("Current Balance:", f"{self._balance:.2f}"))
        print("%-25s%s" % ("Status:", f"{self.status}"))

        for i in BudgetTypes:
            self.get_transaction_by_budget(i)

    def add_budget(self):
        """
        Create budget objects for each budget category and store the
        budget objects in a list in the bank account object
        """
        for i in BudgetTypes:
            # total_budget must be a float
            total_budget = float(input(f"Enter the total budget for "
                                       f"'{BudgetTypes(i).name}' "
                                       f"category: "))

            self.budgets.append(Budget(BudgetTypes(i).name,
                                       total_budget))

    def get_budget_details(self):
        """
        Print the details of each budget by its category
        """
        print("\n" + "-" * 100)
        print("Your Budget Details")
        print("-" * 100)
        print("%-20s%-20s%-20s%-20s%s" % ("Budget Category",
                                          "Total Budget",
                                          "Budget Spent",
                                          "Budget Remaining",
                                          "Status"))
        for budget in self.budgets:
            print(budget)

    def get_transaction_by_budget(self, budget_type):
        """
        Print out transaction details for a budget type
        :param budget_type:
        :return:
        """
        budget_name = BudgetTypes(budget_type).name
        print("\n" + "-" * 100)
        print(f"Transaction Details for {budget_name}:")
        print("-" * 100)

        if self.trans_list[f"{budget_name}"]:
            print("%-30s%-20s%-20s%s" % ("Timestamp", "Amount",
                                         "Category", "Shop Name"))
            for transaction in self.trans_list[f"{budget_name}"]:
                print(transaction)
        else:
            print("No transactions have been processed for this category.")

    def process_transaction(self, amount, budget_type, shop_name):
        """
        Process transactions that are verified and store the processed
        transaction objects as a list in the dictionary in the bank
        account object. When transactions are processed, the balance in
        the bank account and the budget amount get decreased by the
        amount spent.
        :param amount: amount to spend as a float
        :param budget_type: budget type as an integer
        :param shop_name: name of the shop as a String
        """
        budget_name = BudgetTypes(budget_type).name

        if self.verify_transaction(amount, budget_type):
            trans = Transaction(amount, budget_name, shop_name)

            self._balance = self._balance - trans.amount

            for budget in self.budgets:
                if budget.budget_type == budget_name:
                    budget.budget_spent = \
                        budget.budget_spent + trans.amount
                    budget.budget_remaining = \
                        budget.budget_remaining - amount

            self.trans_list[f"{budget_name}"] \
                .append(trans)

            print("\n%-30s%-20s%-20s%s" % ("Timestamp", "Amount",
                                           "Category", "Shop Name"))
            for transaction in self.trans_list[f"{budget_name}"]:
                print(transaction)
        else:
            print("Transaction cannot be processed.")

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
        if amount > self.balance:
            print("\nYou cannot spend more than what you have! "
                  "Please check your bank account balance.")
            return False
        if budget.is_locked:
            print("\nYour budget is locked for this category.")
            return False
        return True

    def lock_budget(self, limit, budget_type):
        """
        Change the status of a budget to locked if the the budget limit
        is exceeded.
        :param limit: limit of the budget as a float
        :param budget_type: budget type as an integer
        """
        budget = self.budgets[budget_type - 1]
        if budget.budget_spent >= budget.total_budget * limit \
                and not budget.is_locked:
            budget.is_locked = True
            self.num_locked = self.num_locked + 1
            print(f"\n[CRITICAL]"
                  f"\nYour budget for {budget.budget_type} category has been "
                  f"locked."
                  f"\nYou can no longer spend money for this category.")

    def get_num_locks(self):
        """
        Return the number of the budgets locked
        :return: number of the budgets locked as an integer
        """
        return self.num_locked

    def verify_budget_limit(self, budget_type):
        """
        Verify if the budget limit has been exceeded or not
        :param budget_type: budget type as an integer
        :return:True if the user exceeded the budget limit
        """
        budget = self.budgets[budget_type - 1]
        if budget.budget_remaining <= 0:
            return True
        return False

    def verify_warning_level(self, budget_type, level):
        """
        Verify if the user has exceeded the warning level of the budget
        :param budget_type: budget type as an integer
        :param level: warning level as a float
        :return: True if the user exceeded the warning level
        """
        budget = self.budgets[budget_type - 1]
        warning_level = budget.total_budget - (budget.total_budget * level)
        if warning_level >= budget.budget_remaining > 0:
            return True
        return False

    def add_test_budgets(self):
        """
        Adds budgets to the test user. All budget information are
        hard-coded for testing purpose.
        """
        test_budget_1 = Budget(BudgetTypes(1).name, 100)
        test_budget_2 = Budget(BudgetTypes(2).name, 100)
        test_budget_3 = Budget(BudgetTypes(3).name, 100)
        test_budget_4 = Budget(BudgetTypes(4).name, 100)

        self.budgets.append(test_budget_1)
        self.budgets.append(test_budget_2)
        self.budgets.append(test_budget_3)
        self.budgets.append(test_budget_4)
