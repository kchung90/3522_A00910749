"""
A simple card management application.
"""

from datetime import date


class Card:
    """
    Represent a Card that is stored in the wallet. A Card object has a
    cardholder name, expiry date, and the id number.
    """
    def __init__(self, cardholder_name, expiry_date, id_number):
        """
        Construct a Card
        :param cardholder_name: name of the cardholder as a String
        :param expiry_date: expiry date of the card as a String
        :param id_number: ID Number of the card as a String
        :precondition: id_number must be 9 characters long, start with
        "ARD", and the contains last 6 characters as digits
        """
        self.cardholder_name = cardholder_name
        self.expiry_date = expiry_date
        if len(id_number) == 9 and id_number[0:3] == "ARD"\
                and id_number[3:].isdigit():
            self.id_number = id_number
        else:
            print("Please enter a valid ID number")

    def __str__(self):
        """
        Return the description of the card object.
        :return: description of the Card object as a String
        """
        return f"Cardholder Name: {self.cardholder_name}\n" \
               f"Expiry Date: {self.expiry_date}\n" \
               f"ID Number: {self.id_number}"

    def access_card(self):
        """
        Check if the card can be accessed or not
        :return: True if the card's expiry date is greater than the
        today's date
        """
        if self.expiry_date > date.today():
            return True
        else:
            return False


class Person:
    """
    Represent a Person who holds the wallet.
    """
    def __init__(self, name, date_of_birth):
        """
        Construct a Person object
        :param name: name of the person as a String
        :param date_of_birth: date of the birth as a String
        """
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        """
        Return the description of the Person object
        :return: description of the Person object as a String
        """
        return f"Name of Person: {self.name}\n" \
               f"Date of Birth: {self.date_of_birth}"


class Wallet:
    """
    Represent a Wallet which holds cards
    """
    def __init__(self, owner):
        """
        Construct a Wallet object
        :param owner: owner of the wallet as a Person
        """
        self.owner = owner
        self.cards = {}

    def remove(self, id_number):
        """
        Remove a card from a wallet with the input id number.
        :param id_number: id number of the card as a String
        :return: a Card object that is removed if the card is found,
        or None if the card is not found.
        """
        if id_number in self.cards:
            return self.cards.pop(id_number)
        else:
            return None

    def search(self, id_number):
        """
        Search a card from a wallet with the input id number.
        :param id_number: id number of the card as a String
        :return: a Card object if the card is found, or None if the
        card is not found.
        """
        if id_number in self.cards.keys():
            return self.cards[id_number]
        else:
            return None

    def add(self, a_card):
        """
        Add a card to the wallet if it does not exist in the wallet
        already.
        :param a_card: a Card object to be added to the wallet
        :return: a Card object that is added to the wallet
        """
        if self.search(a_card.id_number):
            print("Card already exists in the wallet.")
        else:
            self.cards[a_card.id_number] = a_card
            return a_card

    def __str__(self):
        """
        Return the description of the Wallet object.
        :return: description of the wallet object
        """
        card_list = ""
        for key in self.cards:
            card_list += f"{self.cards[key]}\n"

        return f"- Wallet Owner:\n{self.owner}\n" \
               f"- Card Information:\n{card_list}"


def main():
    """
    Create a wallet, person, and 2 cards to drive the program.
    """
    owner = Person("Captain America", date(1900, 11, 11))
    wallet = Wallet(owner)
    card1 = Card("Hulk", date(2023, 1, 1), "ARD123456")
    card2 = Card("Iron Man", date(2023, 2, 2), "ARD654321")

    print(wallet.add(card1))
    print(wallet.add(card2))

    print(wallet)

    print("- Search Card 'ARD123456':")
    print(wallet.search("ARD123456"))

    print("- Remove Card 'ARD123456':")
    print(wallet.remove("ARD123456"))

    print("- Search Card 'ARD123456':")
    print(wallet.search("ARD123456"))

    print("- Card can be accessed?")
    print(card1.access_card())


if __name__ == '__main__':
    main()
