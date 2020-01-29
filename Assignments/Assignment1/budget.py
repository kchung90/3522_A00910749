import enum


class Budget:

    def __init__(self, total_budget, budget_type, amount_spent, amount_left,
                 is_locked=False):
        self.is_locked = is_locked
        self.total_budget = total_budget
        self.amount_spent = amount_spent
        self.amount_left = amount_left
        self.budget_type = budget_type


class BudgetTypes(enum.Enum):
    GAMES = 1
    CLOTHING = 2
    FOOD = 3
    MISC = 4
