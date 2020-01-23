"""
This module creates a wallet which can hold multiple cards of a person.
"""

from datetime import date


class Card:
    """
    Represent a Card that is stored in the wallet. A Card object has a
    cardholder name, expiry date, and the id number.
    """
    def __init__(self, cardholder_name, id_number, expiry_date):
        """
        Construct a Card
        :param cardholder_name: name of the cardholder as a String
        :param id_number: ID Number of the card as a String
        :param expiry_date: expiry date of the card as a Date
        """
        self.cardholder_name = cardholder_name
        self._id_number = id_number
        self.expiry_date = expiry_date

    @property
    def id_number(self):
        """
        Return the ID number of the card.
        :return: ID number of the card as a String
        """
        return self._id_number

    def __str__(self):
        """
        Return the description of the card object.
        :return: description of the Card object as a String
        """
        return f"Cardholder Name: {self.cardholder_name}\n" \
               f"ID Number: {self.id_number}\n" \
               f"Expiry Date: {self.expiry_date}"

    def access_card(self):
        """
        Check if the card can be accessed or not by checking the expiry
        date. Return True if the card's expiry date is future.
        :return: True if the card is valid. False if the card is
        invalid
        """
        if self.expiry_date > date.today():
            return True
        else:
            return False


class Person:
    """
    Represent a Person who holds the wallet. A person object has a name
    and date of birth.
    """
    def __init__(self, name, date_of_birth):
        """
        Construct a Person object
        :param name: name of the person as a String
        :param date_of_birth: date of the birth as a Date
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
        :return: a Card object that is removed, or None if the card is
        not found.
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
        :return: description of the wallet object as a String
        """
        card_list = ""
        for key in self.cards:
            card_list += f"{self.cards[key]}\n"

        return f"- Wallet Owner:\n{self.owner}\n" \
               f"- Card Information:\n{card_list}"


def main():
    """
    Create a wallet, a person, and 2 cards to drive the program.
    """
    owner = Person("Captain America", date(1900, 11, 11))
    wallet = Wallet(owner)
    card_1 = Card("Hulk", "ARD123456", date(2023, 1, 1))
    card_2 = Card("Iron Man", "ARD654321", date(2023, 2, 2))

    print("- Add the first card:")
    print(wallet.add(card_1))
    print("- Add the second card:")
    print(wallet.add(card_2))

    print(wallet)

    print("- Search Card 'ARD123456':")
    print(wallet.search("ARD123456"))

    print("- Remove Card 'ARD123456':")
    print(wallet.remove("ARD123456"))

    print("- Search Card 'ARD123456' which was removed:")
    print(wallet.search("ARD123456"))

    print("- Card can be accessed?")
    print(card_1.access_card())


if __name__ == '__main__':
    main()
