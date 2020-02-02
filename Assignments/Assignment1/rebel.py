from Assignments.Assignment1.user import User


class Rebel(User):

    def __init__(self, name, age, user_type):
        super().__init__(name, age)
        self.user_type = user_type

    def record_transaction(self, amount, category, shop_name):
        self.bank_account.process_transaction(amount, category, shop_name)
        self.bank_account.lock_budget()
