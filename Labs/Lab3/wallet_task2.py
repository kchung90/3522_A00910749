"""
A simple card management application.
"""
import abc
from datetime import date


class Card(abc.ABC):
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
        return self._id_number

    @abc.abstractmethod
    def __str__(self):
        """
        Return the description of the card object.
        :return: description of the Card object as a String
        """
        pass

    @abc.abstractmethod
    def access_card(self):
        """
        Check if the card can be accessed or not
        :return: True if the card's expiry date is greater than the
        today's date
        """
        pass


class Person:
    """
    Represent a Person who holds the wallet.
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


class IDCard(Card):
    def __init__(self, cardholder_name, id_number, expiry_date, date_of_birth):
        super().__init__(cardholder_name, id_number, expiry_date)
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Cardholder Name: {self.cardholder_name}\n" \
               f"ID Number: {self.id_number}\n" \
               f"Expiry Date: {self.expiry_date}\n" \
               f"Date of Birth: {self.date_of_birth}"

    def access_card(self):
        if len(self.id_number) == 9 and self.id_number[0:3] == "ARD"\
                and self.id_number[3:].isdigit() \
                and self.expiry_date > date.today():
            return True
        else:
            return False


class CreditCard(Card):
    def __init__(self, name, id_number, expiry_date, balance, cvv):
        super().__init__(name, id_number, expiry_date)
        self.balance = balance
        self.cvv = cvv

    def __str__(self):
        return f"Cardholder Name: {self.cardholder_name}\n" \
               f"ID Number: {self.id_number}\n" \
               f"Expiry Date: {self.expiry_date}\n" \
               f"Balance: {self.balance}\n" \
               f"CVV: {self.cvv}"

    def access_card(self):
        if len(self.id_number) == 16 and self.id_number.isdigit() \
                and self.expiry_date > date.today():
            charge_amount = float(input("Enter the amount to charge: "))
            if charge_amount < self.balance:
                self.balance -= charge_amount
            return True
        else:
            return False


def main():
    """
    Create a wallet, a person, and 2 cards to drive the program.
    """
    owner = Person("Homer Simpson", date(1960, 12, 12))
    wallet = Wallet(owner)
    card1 = IDCard("Bart", "ARD123456", date(2023, 1, 1), date(1980, 1, 1))
    card2 = CreditCard("Lisa", "1234123412341234", date(2023, 1, 1), 100.00,
                       123)

    print("- Add Card 1")
    print(wallet.add(card1))

    print("- Add Card 2")
    print(wallet.add(card2))

    print("- Access Card 1")
    print(card1.access_card())

    print("- Access Card 2")
    print(card2.access_card())

    print(wallet)

    print("- Search for Card '1234123412341234'")
    print(wallet.search("1234123412341234"))

    print("- Remove Card '1234123412341234'")
    print(wallet.remove("1234123412341234"))

    print("- Search for Card '1234123412341234'")
    print(wallet.search("1234123412341234"))

    # print(card2)


if __name__ == '__main__':
    main()
