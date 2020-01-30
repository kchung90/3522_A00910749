from Assignments.Assignment1.budget import BudgetTypes, Budget
from Assignments.Assignment1.transaction import Transaction


class BankAccount:

    def __init__(self, name, account_number, balance):
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
        return self._balance

    def add_budget(self):
        for i in BudgetTypes:
            input_total_budget = float(input(f"Enter the total budget for "
                                             f"'{BudgetTypes(i).name}' "
                                             f"category: "))
            self.budgets.append(Budget(BudgetTypes(i).name,
                                       input_total_budget))

    def create_transaction(self):
        input_trans_amount = float(input("\nEnter the amount spent: "))
        input_trans_category = int(input(f"Select a category:\n"
                                         f"1) {BudgetTypes(1).name}\n"
                                         f"2) {BudgetTypes(2).name}\n"
                                         f"3) {BudgetTypes(3).name}\n"
                                         f"4) {BudgetTypes(4).name}\n"))
        trans_category = BudgetTypes(input_trans_category).name
        input_shop_name = input("Enter the name of the shop: ")

        if self.verify_transaction(input_trans_amount):
            transaction = Transaction(input_trans_amount,
                                      trans_category, input_shop_name)

            self._balance = self._balance - transaction.amount

            for budget in self.budgets:
                if budget.budget_type == trans_category:
                    budget.total_budget = budget.total_budget \
                                          - transaction.amount

            self.trans_list[f"{trans_category}"] \
                .append(transaction)

            print("\n%-25s%-15s%-15s%s" % ("Timestamp", "Amount",
                                           "Category", "Shop Name"))
            for transaction in self.trans_list[f"{trans_category}"]:
                print(transaction)
        else:
            print("\nTransaction is not valid. Cannot be processed!")

    def verify_transaction(self, amount):
        if amount > self.balance:
            return False
        return True
