from Assignments.Assignment1.user import User


class Troublemaker(User):

    def __init__(self, name, age, user_type):
        super().__init__(name, age)
        self.user_type = user_type