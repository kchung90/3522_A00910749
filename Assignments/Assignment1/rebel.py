from Assignments.Assignment1.user import User


class Rebel(User):

    def __init__(self, name, age, user_type):
        super().__init__(name, age)
        self.user_type = user_type