"""
This module houses the library Catalogue system. The LibraryCatalogue is
a high level module that is responsible for the loading, and perusal of
LibraryItems.
"""
from Labs.Lab8.item_loader import FactoryMapper
from Labs.Lab8.items import InvalidNumCopiesError, InvalidCallNumberError


class LibraryCatalogue:
    """
    A Catalogue is responsible for maintaining, loading and viewing the
    collection of items found in a library.
    """

    def __init__(self, item_list=None):
        """
        Intialize the catalogue with a list of Items.
        :param item_list: a sequence of Item objects.
        """
        if not item_list:
            self._item_list = []
        else:
            self._item_list = item_list

    def display_catalogue_menu(self):
        """
        Display the interactive Catalogue menu. The user is given
        the choice to add, remove, find and display items in the
        catalogue.
        """
        print("\nWelcome to the Catalogue!")
        print("------------------------")
        user_input = None
        while user_input != 4:
            print("\nWhat would you like to do?")
            print("1. Find an item")
            print("2. Load items from file")
            print("3. Display Entire Catalogue")
            print("4. Exit")
            user_input = int(input("Enter you choice (1-5): "))

            if user_input == 1:
                input_data = input("Enter the title or call_number of the "
                                   "item:")
                found_items = self.find_items(input_data)
                print("We found the following:")
                if len(found_items) > 0:
                    for item in found_items:
                        print(item)
                else:
                    print("Sorry! We found nothing that matches the input")

            elif user_input == 2:
                try:
                    self.load_items()
                except InvalidNumCopiesError as e:
                    print(e)
                except InvalidCallNumberError as e:
                    print(e)

            elif user_input == 3:
                self.display_available_items()

            elif user_input == 4:
                pass
            else:
                print("Could not process input. ")
        print("Thanks for dropping by!")

    def find_items(self, input_data):
        """
        Find items with the same and similar title.
        :param input_data: a string
        :return: a list of matching LibraryItems.
        """
        results = [item
                   for item in self._item_list
                   if input_data == item._title or
                   input_data == item._call_number]
        return results

    def load_items(self):
        """
        Items are read from an excel file and are added to the item
        list.
        """
        factory_mapper = FactoryMapper()

        for i in factory_mapper.execute_factory_menu().get_next_item():
            self._item_list.append(i)

    def display_available_items(self):
        """
        Display all the items in the catalogue.
        """
        print("Catalogue List")
        print("--------------", end="\n\n")
        for library_item in self._item_list:
            print(library_item)


def main():
    """
    Drives the program
    """
    catalogue = LibraryCatalogue()
    catalogue.display_catalogue_menu()


if __name__ == '__main__':
    main()
