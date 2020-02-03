from Assignments.Assignment1.user import User


class Rebel(User):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.warning_level = 0.5

    def record_transaction(self, amount, category, shop_name):
        self.bank_account.process_transaction(amount, category, shop_name)
        self.bank_account.lock_budget(1)
        self.overage_notification(category)
        self.warning_notification(category)

    def overage_notification(self, category):
        if self.bank_account.verify_budget_limit(category):
            print("\nYOU CAN NO LONGER SPEND MONEY FOR THIS CATEGORY!"
                  "\nYOUR MAXIMUM BUDGET FOR THIS CATEGORY HAS BEEN REACHED!")

    def warning_notification(self, category):
        if self.bank_account\
                .verify_warning_level(category, self.warning_level):
            print(f"\nYou have exceeded {self.warning_level * 100:.0f}% of "
                  f"your budget for this category.")
