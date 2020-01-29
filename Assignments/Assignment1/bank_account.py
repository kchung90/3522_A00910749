from datetime import datetime
from Assignments.Assignment1.budget import BudgetTypes


class BankAccount:

    def __init__(self, name, account_number, balance, budgets):
        self.name = name
        self.account_number = account_number
        self._balance = balance
        self.budgets = budgets
        self.trans_list = {BudgetTypes(1).name: [],
                           BudgetTypes(2).name: [],
                           BudgetTypes(3).name: [],
                           BudgetTypes(4).name: []}

    @property
    def balance(self):
        return self._balance

    def process_transaction(self, transaction):
        if self.verify_transaction(transaction):
            category = int(transaction.budget_category)
            self.trans_list[f"{BudgetTypes(category).name}"]\
                .append(transaction)
        else:
            print("Transaction is not valid. Cannot be processed!")

    def verify_transaction(self, transaction):
        if transaction.timestamp > datetime.today():
            return False
        if transaction.amount > self.balance:
            return False
        return True
