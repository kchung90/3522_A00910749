'''
This module takes in user input to add, subtract, divide, or multiply
2 numbers.
'''


def add(a, b):
    """
    Adds two numbers
    :param a: an int
    :param b: an int
    :return: the sum of the two numbers as an int
    """
    return a + b


def subtract(a, b):
    """
    Subtracts two numbers
    :param a: an int
    :param b: an int
    :return: the difference of the two numbers as an int
    """
    return a - b


def divide(a, b):
    """
    Divides two numbers
    :param a: an int
    :param b: an int
    :return: the quotient of the two numbers as an int
    """
    return a / b


def multiply(a, b):
    """
    Multiplies two numbers
    :param a: an int
    :param b: an int
    :return: the product of the two numbers as an int
    """
    return a * b


def main():
    """
    Runs the program to add, subtract, divide, or multiply
    :return: the answer as an int
    """
    print("Menu\n1) Add\n2) Subtract\n3) Divide\n4) Multiply\n5) Exit")
    user_input = int(input("Enter an option: "))

    while user_input != 5:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        input_map = {
            1: add,
            2: subtract,
            3: divide,
            4: multiply
        }

        result = input_map[user_input](a, b)
        print(f"Your answer is {result}\n")

        main()


if __name__ == '__main__':
    main()
