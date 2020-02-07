"""
@author Kevin Chung

This module drives the Family Appointed Moderator (F.A.M.) program
which monitors the user's expenses for each category of budget.

This module provides the UI to enter user inputs to select menu options
to perform desired tasks.
"""
from Assignments.Assignment1.user import Angel, Troublemaker, Rebel


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
        user_name = input("\nEnter the user's name: ")
        # user_age must be a positive integer
        user_age = int(input("Enter the user's age: "))

        # user_type must be a positive integer
        input_user_type = None
        while input_user_type != 1 and input_user_type != 2 and \
                input_user_type != 3:
            input_user_type = int(input("Enter the type of the user:\n"
                                        "1) Angel\n"
                                        "2) Troublemaker\n"
                                        "3) Rebel\n"))

        if input_user_type == 1:
            self.user = Angel(user_name, user_age)
        elif input_user_type == 2:
            self.user = Troublemaker(user_name, user_age)
        elif input_user_type == 3:
            self.user = Rebel(user_name, user_age)

        self.user.add_bank_account()

    def start(self):
        """
        Show menu prompts to the user. A user can perform actions by
        following the prompts until he decides to exit the program.

        :precondition: a user must input correct type for each prompt
        """
        print("-" * 100)
        print("{0:^100}".format("Family Appointed Moderator"))
        print("-" * 100)

        # start_menu must be a positive integer
        start_menu = None
        while start_menu != 1 and start_menu != 2:
            print("\nStart Menu:"
                  "\n1) Register a New User"
                  "\n2) Load a Test User")
            start_menu = int(input("Select your option: "))
            if start_menu == 1:
                self.register_user()
            elif start_menu == 2:
                self.user = Rebel.load_test_user()

        self.main_menu()

    def main_menu(self):
        """
        Display main menu to the user. User can select menu options to
        view their budgets, record transactions, view transactions by
        budget, and view bank account details.
        """
        # main_menu must be a positive integer
        main_menu = None
        while main_menu != 5:
            print("\nMain Menu:"
                  "\n1) View Budgets"
                  "\n2) Record Transaction"
                  "\n3) View Transactions by Budget"
                  "\n4) View Bank Account Details"
                  "\n5) Quit")
            main_menu = int(input("Select your option: "))
            if main_menu == 1:
                self.user.view_budgets()
            elif main_menu == 2:
                # trans_amount must be a positive number
                trans_amount = float(input("\nEnter the amount spent: "))
                # budget_type must be a positive integer
                budget_type = None
                while budget_type != 1 and budget_type != 2 and \
                        budget_type != 3 and budget_type != 4:
                    budget_type = int(input("Select a category:\n"
                                            "1) GAMES\n"
                                            "2) CLOTHING\n"
                                            "3) FOOD\n"
                                            "4) MISC\n"))
                shop_name = input("Enter the name of the shop: ")

                self.user.record_transaction(trans_amount,
                                             budget_type,
                                             shop_name)
            elif main_menu == 3:
                # budget_type must be a positive integer
                budget_type = None
                while budget_type != 1 and budget_type != 2 and \
                        budget_type != 3 and budget_type != 4:
                    budget_type = int(input("\nSelect a category to "
                                            "view transactions:\n"
                                            "1) GAMES\n"
                                            "2) CLOTHING\n"
                                            "3) FOOD\n"
                                            "4) MISC\n"))
                self.user.view_trans_by_budget(budget_type)
            elif main_menu == 4:
                self.user.view_bank_account_details()


def main():
    """
    Drives the program by creating a Driver object and calling the
    start() method
    """
    driver = Driver()
    driver.start()


if __name__ == '__main__':
    main()
