"""
This module contains all the classes that are responsible or have
something to do with the creation of LibraryItems. Classes currently
implemented:
    - FactoryMapper
      Client facing class used to retrieve the right factory class
"""
import abc
from Labs.Lab8.items import Manga, Game, Movie
import pandas


class LibraryItemFactory(abc.ABC):

    def __init__(self, path):
        self.path = path

    @abc.abstractmethod
    def get_next_item(self):
        pass


class MangaFactory(LibraryItemFactory):
    def get_next_item(self):
        my_file = pandas.read_excel(self.path)

        for item, row in my_file.iterrows():
            yield Manga(**row.to_dict())


class GameFactory(LibraryItemFactory):
    def get_next_item(self):
        my_file = pandas.read_excel(self.path)

        for item, row in my_file.iterrows():
            yield Game(**row.to_dict())


class MovieFactory(LibraryItemFactory):
    def get_next_item(self):
        my_file = pandas.read_excel(self.path)

        for item, row in my_file.iterrows():
            yield Movie(**row.to_dict())


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

        file_name = input("\nEnter file name of the excel file to load from:")
        return factory_type(file_name)


if __name__ == '__main__':
    df = pandas.read_excel("manga_data.xlsx")
