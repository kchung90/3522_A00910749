"""
This module drives the Family Appointed Moderator program which
monitors the user's expenses to not exceed the budget in each category.
"""
from Assignments.Assignment1.user import User


class Driver:
    """
    Driver class interacts with the user by providing the menu. A user
    can register to the program by following the menu options.
    """
    def __init__(self):
        """
        Initializes the Driver object
        """
        self.user = None

    def register_user(self):
        """
        Register a user to the program.
        """
        input_name = input("\nEnter the user's name: ")
        input_age = int(input("Enter the user's age: "))

        self.user = User(input_name, input_age)
        self.user.add_bank_account()

    def run(self):
        print("-" * 50)
        print("{0:^50}".format("Family Appointed Moderator"))
        print("-" * 50)
        print("\nPlease select an option:")
        input_option = int(input("1) Register a new user\n"
                                 "2) Load test users\n"))

        if input_option == 1:
            self.register_user()
        elif input_option == 2:
            self.user = User.load_test_users()

        input_menu = None

        while input_menu != 2:
            input_menu = int(input("\nSelect the following menu:\n"
                                   "1) Record Transaction\n"
                                   "2) Quit\n"))
            if input_menu == 1:
                self.record_transaction()

    def record_transaction(self):
        self.user.bank_account.create_transaction()


def main():
    driver = Driver()
    driver.run()


if __name__ == '__main__':
    main()
