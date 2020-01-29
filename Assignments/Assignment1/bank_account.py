class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def process_transaction(self):
        pass

    def verify_transaction(self):
        pass
