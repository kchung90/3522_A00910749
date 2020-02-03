from Assignments.Assignment1.user import User


class Rebel(User):

    def __init__(self, name, age, user_type):
        super().__init__(name, age)
        self.user_type = user_type

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
        if self.bank_account.verify_warning_level(category, 0.5):
            print("\nYou have exceeded 50% of your budget for this category.")