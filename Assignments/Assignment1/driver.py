from Assignments.Assignment1.user import User


class Driver:

    def __init__(self):
        self.user = None

    def register_user(self):
        input_name = input("Enter the user's name: ")
        input_age = int(input("Enter the user's age: "))

        self.user = User(input_name, input_age)
        self.user.add_bank_account()

    def run(self):
        print("Please select an option:")
        input_option = int(input("1) Register a new user\n"
                                 "2) Load test users\n"))

        if input_option == 1:
            self.register_user()
        elif input_option == 2:
            self.user = User.load_test_users()

        input_menu = int(input("Select the following menu:\n"
                               "1) Record Transaction\n"))
        if input_menu == 1:
            self.record_transaction()

    def record_transaction(self):
        self.user.bank_account.create_transaction()


def main():
    driver = Driver()
    driver.run()


if __name__ == '__main__':
    main()
