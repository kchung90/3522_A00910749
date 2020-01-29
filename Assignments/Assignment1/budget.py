import enum


class Budget:

    def __init__(self, budget_type, total_budget, is_locked=False):
        self.budget_type = budget_type
        self.total_budget = total_budget
        self.amount_spent = 0
        self.amount_left = 0
        self.is_locked = is_locked


class BudgetTypes(enum.Enum):
    GAMES = 1
    CLOTHING = 2
    FOOD = 3
    MISC = 4
