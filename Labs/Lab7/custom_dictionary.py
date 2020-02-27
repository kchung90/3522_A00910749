"""
@author Kevin Chung

This module depicts a dictionary which contains list of words and
definitions imported from a text file. Words that are queried by a user
are exported out to a new text file. This module also handles any
possible errors raised while running the code.
"""
from difflib import get_close_matches


class CustomDictionary:
    """
    Represents a custom dictionary which contains a list of words and
    definitions imported from a text file.
    """

    def __init__(self, path):
        """
        Initializes the CustomDictionary object by importing data from
        a text file.
        If a file cannot be found in path, FileNotFoundError is raised.
        If the data inside the file is not in the correct format,
        ImportError is raised.
        :param path: path of the text file as a String
        """
        with open(path, mode="r", encoding="utf-8") as my_file:
            f = my_file.read()
            if "--" not in f or "\n" not in f:
                raise ImportError
            else:
                data = [line.split("\n") for line in
                         list(f.split("--"))]
        self.definitions = {value[0]: value[1:] for value in data
                            if value != [""]}
        self.words_queried = []

    def query(self, word):
        """
        Returns the definition of the word queried by the user and
        store the queried word in a list.
        If a word is not found in a dictionary, WordNotFoundError is
        raised.
        :param word: word as a String
        :return: the definition of the word as a String
        """
        closest_word = get_close_matches(word.lower(),
                                         list(self.definitions.keys()))
        if not closest_word:
            raise WordNotFoundError(word)
        else:
            if closest_word[0] not in self.words_queried:
                self.words_queried.append(closest_word[0])
            str_formatted = ""
            for definition in self.definitions[closest_word[0]]:
                if definition != "":
                    str_formatted += definition + "\n"
            return str_formatted

    def export(self):
        """
        Exports the queried words and their definitions to a new text
        file.
        """
        with open("word_queries.txt", mode="w", encoding="utf-8") as my_file:
            for word in self.words_queried:
                my_file.write("--" + word + "\n")
                for definition in self.definitions[word]:
                    if definition != "":
                        my_file.write(definition + "\n")


class WordNotFoundError(Exception):
    """
    Represents a exception when a word inside the dictionary cannot be
    found.
    """
    def __init__(self, missing_word):
        """
        Initializes the WordNotFoundError. Stores the missing word in
        the dictionary and prints out the missing word.
        :param missing_word: word that is not found in the dictionary
        as a String
        """
        self.missing_word = missing_word
        super().__init__(f"'{self.missing_word}' is not found in the file.")


def main():
    """
    Drives the program by initializing the CustomDictionary object and
    querying the words. Exceptions are handled in main()
    """
    try:
        my_dict = CustomDictionary("data.txt")
        my_dict.query("zodiac")
        my_dict.query("computational linguistics")
        my_dict.query("computational linguistics")
        my_dict.query("rain")
        my_dict.query("COFFee")
        my_dict.query("coffee")
        my_dict.query("rain")
        # my_dict.query("asdf1234")
    except FileNotFoundError:
        print("File is not found")
    except ImportError:
        print("Entries in the file are not in a correct format to use the "
              "methods in this module.")
    except WordNotFoundError as e:
        print(e)
    else:
        my_dict.export()


if __name__ == '__main__':
    main()
