from Assignments.Assignment1.bank_account import BankAccount
from Assignments.Assignment1.budget import Budget
from Assignments.Assignment1.budget import BudgetTypes


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.bank_account = None

    def add_bank_account(self):
        input_bank_name = input("Enter the user's bank name: ")
        input_account_num = int(input("Enter the user's "
                                      "bank account number: "))
        input_bank_balance = float(input("Enter the user's bank balance: "))

        self.bank_account = BankAccount(input_bank_name, input_account_num,
                                        input_bank_balance)
        self.bank_account.add_budget()

    @classmethod
    def load_test_users(cls):
        test_user = User("Test User", 20)

        test_user.bank_account = BankAccount("Scotiabank", "4536000011112222",
                                          500)

        test_budget_1 = Budget(BudgetTypes(1).name, 100)
        test_budget_2 = Budget(BudgetTypes(2).name, 100)
        test_budget_3 = Budget(BudgetTypes(3).name, 200)
        test_budget_4 = Budget(BudgetTypes(4).name, 100)

        test_user.bank_account.budgets.append(test_budget_1)
        test_user.bank_account.budgets.append(test_budget_2)
        test_user.bank_account.budgets.append(test_budget_3)
        test_user.bank_account.budgets.append(test_budget_4)

        return test_user
