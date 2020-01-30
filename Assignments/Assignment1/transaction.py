from datetime import datetime


class Transaction:

    def __init__(self, amount, budget_category, shop_name):
        self.amount = amount
        self.budget_category = budget_category
        self.shop_name = shop_name
        self.timestamp = datetime.today().replace(microsecond=0)

    def __str__(self):
        return "%-25s%-15s%-15s%s" % (f"{self.timestamp}",
                                      f"{self.amount:.2f}",
                                      f"{self.budget_category}",
                                      f"{self.shop_name}")
