from Assignments.Assignment1.user import User


class Angel(User):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.warning_level = 0.9

    def record_transaction(self, amount, category, shop_name):
        self.bank_account.process_transaction(amount, category, shop_name)
        self.overage_notification(category)
        self.warning_notification(category)

    def overage_notification(self, category):
        if self.bank_account.verify_budget_limit(category):
            print("\nYou have exceeded your total budget for this category.")

    def warning_notification(self, category):
        if self.bank_account\
                .verify_warning_level(category, self.warning_level):
            print(f"\nYou have exceeded {self.warning_level * 100:.0f}% of "
                  f"your budget for this category.")
