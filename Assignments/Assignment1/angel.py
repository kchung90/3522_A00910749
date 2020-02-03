from Assignments.Assignment1.bank_account import BankAccount
from Assignments.Assignment1.user import User


class Angel(User):

    def __init__(self, name, age):
        super().__init__(name, age)

    def record_transaction(self, amount, category, shop_name):
        self.bank_account.process_transaction(amount, category, shop_name)
        self.overage_notification(category)
        self.warning_notification(category)

    def overage_notification(self, category):
        if self.bank_account.verify_budget_limit(category):
            print("\nYou have exceeded your total budget for this category.")

    def warning_notification(self, category):
        if self.bank_account.verify_warning_level(category, 0.9):
            print("\nYou have exceeded 90% of your budget for this category.")

    @classmethod
    def load_test_user(cls):
        """
        Initialize a test user by hardcoding the information for a
        testing purpose.
        A test user has all the information including the bank account
        and budget information.
        :return: a test user as a User object
        """
        test_user = Angel("Test User", 20)
        test_user.bank_account = BankAccount("Scotiabank", "4536000011112222",
                                             500)
        test_user.bank_account.get_test_user_budgets()

        return test_user
