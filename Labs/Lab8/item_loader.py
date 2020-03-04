"""
This module contains all the classes that are responsible or have
something to do with the creation of LibraryItems. Classes currently
implemented:
    - FactoryMapper
      Client facing class used to retrieve the right factory class
"""
import abc
import pandas
from Labs.Lab8.items import LibraryItem, Manga, Game, Movie


class LibraryItemFactory(abc.ABC):
    """
    Defines the base class of the LibraryItemFactory hierarchy as an
    ABC. All library item factories must inherit from this class and
    implement the get_next_item() method.
    """
    def __init__(self, path):
        """
        Initializes the LibraryItemFactory
        :param path: path of the file as a String
        """
        self.path = path

    @abc.abstractmethod
    def get_next_item(self):
        """
        Generator function that yields the next item in the file. This
        method needs to be overridden by the child classes
        """
        pass


class MangaFactory(LibraryItemFactory):
    """
    Represents the MangaFactory which initializes Manga objects
    """
    def get_next_item(self) -> LibraryItem:
        """
        Reads the excel file and yields the Manga object from the file.
        """
        try:
            my_file = pandas.read_excel(self.path)
            for item, row in my_file.iterrows():
                yield Manga(**row.to_dict())
        except FileNotFoundError:
            print("File is not found. Please check the file name again.")


class GameFactory(LibraryItemFactory):
    """
    Represents the GameFactory which initializes Game objects
    """
    def get_next_item(self) -> LibraryItem:
        """
        Reads the excel file and yields the Game object from the file.
        :return:
        """
        try:
            my_file = pandas.read_excel(self.path)
            for item, row in my_file.iterrows():
                yield Game(**row.to_dict())
        except FileNotFoundError:
            print("File is not found. Please check the file name again.")


class MovieFactory(LibraryItemFactory):
    """
    Represents the MovieFactory which initializes Movie objects
    """
    def get_next_item(self) -> LibraryItem:
        """
        Reads the excel file and yields the Movie object from the file.
        """
        try:
            my_file = pandas.read_excel(self.path)
            for item, row in my_file.iterrows():
                yield Movie(**row.to_dict())
        except FileNotFoundError:
            print("File is not found. Please check the file name again.")


class FactoryMapper:
    """
    FactoryMapper contains the class methods to prompt the user for the
    type of item they wish to acquire and returns a factory that can
    provide the items selected.
    """

    factory_map = {
        1: MangaFactory,
        2: GameFactory,
        3: MovieFactory
    }
    """
    Factory map is a dictionary of type {int, FactoryClass}
    """

    @classmethod
    def execute_factory_menu(cls):
        """
        Prompts the user to select the type of items they wish to load an
        returns the appropriate factory.
        :return: object of type LibraryItemFactory
        """
        print("Item Loader")
        print("-----------")
        print("What kind of items would you like to load?")
        print("1. Manga")
        print("2. Games")
        print("3. Movies")

        user_choice = int(input("Enter your choice (1-3):"))
        factory_type = cls.factory_map[user_choice]
        file_name = input("\nEnter file name of the excel file to "
                          "load from:")
        return factory_type(file_name)


if __name__ == '__main__':
    df = pandas.read_excel("manga_data.xlsx")
