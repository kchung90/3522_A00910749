"""
@author Kevin Chung

This module drives the Family Appointed Moderator (F.A.M.) program
which monitors the user's expenses in each category of budget.

This module provides the UI to enter user inputs to select menu to
perform tasks.
"""
from Assignments.Assignment1.angel import Angel
from Assignments.Assignment1.rebel import Rebel
from Assignments.Assignment1.troublemaker import Troublemaker
from Assignments.Assignment1.user import User


class Driver:
    """
    Driver class interacts with the user by providing the menu and
    asking for user inputs.

    A user can register himself first, then use menu options to perform
    any desired tasks until he decides to exit the program.

    More features on the menu are to be added in the future.
    """
    def __init__(self):
        """
        Initializes the driver object
        """
        self.user = None

    def register_user(self):
        """
        Register a user to the program. Calls a method to add a bank
        account for the user.
        """
        input_name = input("\nEnter the user's name: ")
        input_age = int(input("Enter the user's age: "))

        input_user_type = None
        while input_user_type != 1 and input_user_type != 2 and \
                input_user_type != 3:
            input_user_type = int(input("Enter the type of the user:\n"
                                        "1) Angel\n"
                                        "2) Troublemaker\n"
                                        "3) Rebel\n"))

        if input_user_type == 1:
            self.user = Angel(input_name, input_age, input_user_type)
        elif input_user_type == 2:
            self.user = Troublemaker(input_name, input_age, input_user_type)
        elif input_user_type == 3:
            self.user = Rebel(input_name, input_age, input_user_type)

        self.user.add_bank_account()

    def menu(self):
        """
        Show menu prompts to the user. A user can perform actions by
        following the prompts until he decides to exit the program.

        :precondition: a user must input correct type for each prompt
        """
        print("-" * 50)
        print("{0:^50}".format("Family Appointed Moderator"))
        print("-" * 50)

        input_option = None
        input_menu = None

        while input_option != 1 and input_option != 2:
            print("\nPlease select an option:")
            input_option = int(input("1) Register a new user\n"
                                     "2) Load test users\n"))
            if input_option == 1:
                self.register_user()
            elif input_option == 2:
                self.user = User.load_test_user()

        while input_menu != 5:
            input_menu = int(input("\nSelect the following menu:\n"
                                   "1) View Budgets\n"
                                   "2) Record Transaction\n"
                                   "3) View Transactions by Budget\n"
                                   "4) View Bank Account Details\n"
                                   "5) Quit\n"))
            if input_menu == 1:
                self.user.view_budgets()
            elif input_menu == 2:
                self.user.record_transaction()
            elif input_menu == 3:
                pass
            elif input_menu == 4:
                pass


def main():
    """
    Drives the program by creating a Driver object and calling the
    menu method
    """
    driver = Driver()
    driver.menu()


if __name__ == '__main__':
    main()
