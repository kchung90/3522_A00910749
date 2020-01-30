from datetime import datetime


class Transaction:

    def __init__(self, amount, budget_category, shop_name):
        self.timestamp = datetime.today()
        self.amount = amount
        self.budget_category = budget_category
        self.shop_name = shop_name

    def __str__(self):
        return f"{self.timestamp}\t{self.amount}\t{self.budget_category}\t" \
               f"{self.shop_name}"