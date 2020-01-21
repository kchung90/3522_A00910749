from datetime import date


class Card:

    def __init__(self, cardholder_name, expiry_date, id_number):
        self.cardholder_name = cardholder_name
        self.expiry_date = expiry_date
        if len(id_number) == 9 and id_number[0:3] == "ARD"\
                and id_number[3:].isdigit():
            self.id_number = id_number
        else:
            print("Please enter a valid ID number")

    def __str__(self):
        return f"Cardholder Name: {self.cardholder_name}\n" \
               f"Expiry Date: {self.expiry_date}\n" \
               f"ID Number: {self.id_number}"

    def access_card(self):
        if self.expiry_date > date.today():
            return True
        else:
            return False


class Person:

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Name of Person: {self.name}\n" \
               f"Date of Birth: {self.date_of_birth}"


class Wallet:

    def __init__(self, owner):
        self.owner = owner
        self.cards = {}

    def remove(self, id_number):
        if id_number in self.cards:
            del self.cards[id_number]

    def search(self, id_number):
        if id_number in self.cards.keys():
            return self.cards[id_number]
        else:
            return None

    def add(self, a_card):
        if self.search(a_card.id_number):
            print("Card already exists in the wallet.")
        else:
            self.cards[a_card.id_number] = a_card

    def __str__(self):
        return f"- Wallet Owner:\n{self.owner}\n" \
               f"- Card Information:\n{self.cards}\n"


def main():
    owner = Person("Captain America", date(1900, 11, 11))
    wallet = Wallet(owner)
    card1 = Card("Hulk", date(2023, 1, 1), "ARD123456")
    card2 = Card("Iron Man", date(2023, 2, 2), "ARD654321")

    wallet.add(card1)
    wallet.add(card2)

    print(wallet)

    print(wallet.search("ARD123456"))
    print(wallet.remove("ARD123456"))
    print(wallet.search("ARD123456"))
    print(card1.access_card())






if __name__ == '__main__':
    main()
