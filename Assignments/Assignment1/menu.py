from Assignments.Assignment1.bank_account import BankAccount


class Menu:

    def __init__(self, user):
        self.user = user

    def record_transaction(self, transaction):
        self.user.bank_account.process_transaction(transaction)