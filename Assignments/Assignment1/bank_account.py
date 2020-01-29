from Assignments.Assignment1.budget import BudgetTypes


class BankAccount:

    def __init__(self, name, account_number, balance, budgets):
        self.name = name
        self.account_number = account_number
        self._balance = balance
        self.budgets = budgets
        self.trans_list = {BudgetTypes(1).name: None,
                           BudgetTypes(2).name: None,
                           BudgetTypes(3).name: None,
                           BudgetTypes(4).name: None}

    @property
    def balance(self):
        return self._balance

    def process_transaction(self):
        pass

    def verify_transaction(self):
        pass
