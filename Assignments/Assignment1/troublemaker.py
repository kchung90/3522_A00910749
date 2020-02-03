from Assignments.Assignment1.bank_account import BankAccount
from Assignments.Assignment1.user import User


class Troublemaker(User):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._warning_level = 0.75
        self._lock_level = 1.2

    def get_warning_level(self):
        return self._warning_level

    def get_lock_level(self):
        return self._lock_level

    def record_transaction(self, amount, category, shop_name):
        self.bank_account.process_transaction(amount, category, shop_name)
        self.bank_account.lock_budget(self.get_lock_level())
        self.overage_notification(category)
        self.warning_notification(category)

    def overage_notification(self, category):
        if self.bank_account.verify_budget_limit(category):
            print("\nYou have exceeded your total budget for this category.")

    def warning_notification(self, category):
        if self.bank_account\
                .verify_warning_level(category, self.get_warning_level()):
            print(f"\nYou have exceeded {self.get_warning_level() * 100:.0f}% "
                  f"of your budget for this category.")

    @classmethod
    def load_test_user(cls):
        test_user = Troublemaker("Test User", 20)
        test_user.bank_account = BankAccount("Scotiabank", "4536000011112222",
                                             500)
        test_user.bank_account.add_test_budgets()

        return test_user