class User:

    def __init__(self, name, age, bank_account):
        self.name = name
        self.age = age
        self.bank_account = bank_account

    @classmethod
    def load_test_users(cls):
        pass
