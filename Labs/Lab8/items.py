"""
This module holds the classes that define the data structure of all the
Library Items. The Items currently supported are:
- Manga
- Movies
- Books
These inherit from LibraryItem which is an ABC.
"""
from abc import ABC, abstractmethod


class InvalidNumCopiesError(Exception):
    def __init__(self):
        super().__init__("Number of Copies must be a positive integer.")


class InvalidCallNumberError(Exception):
    def __init__(self, call_num):
        super().__init__(f"{call_num} does not match the correct format for "
                         f"call number.")


class LibraryItem(ABC):
    """
    Defines the base class of the LibraryItem hierarchy as an ABC. All
    library items must inherit from this class and implement the
    __str__ abstract method.
    """

    def __init__(self, title, call_num, num_copies=1):
        """
        :param title: a string
        :param call_num: a string
        :param num_copies: an int
        :precondition num_copies: must be a positive integer.
        """
        self._title = title
        self._call_number = call_num
        if num_copies < 0:
            raise InvalidNumCopiesError
        else:
            self._num_copies = num_copies

    @abstractmethod
    def __str__(self):
        return f"Name: {self._title}, Call Number: {self._call_number}, " \
               f"Availability: {self._num_copies} copies"


class Manga(LibraryItem):
    """
    A manga is a type of LibraryItem that has an artist (String) and
    volume_num (int) as additional fields. All Manga call numbers
    should start with the letter 'M'
    """

    def __init__(self, artist, volume_num, **kwargs):
        """
        :param artist: a String, name of the artist
        :param volume_num: an int
        :param kwargs: Any additional keyword attributes for the base
                       class. Required to have 'title' and 'call_num'.
        :precondition call_num: Call number must follow the format
                                MG.###.###.### where # is a number.
        """
        call_num = kwargs["call_num"]
        if call_num[0:3] == "MG." and call_num[3:6].isdigit() and \
                call_num[7:10].isdigit() and call_num[11:14].isdigit() and \
                call_num[6] == "." and call_num[10] == "." and \
                len(call_num) == 14:
            super().__init__(**kwargs)
            self._artist = artist
            self._volume_num = volume_num
        else:
            raise InvalidCallNumberError(call_num)

    def __str__(self):
        seperator = "-" * 20
        manga_details = f"Type: Manga, Volume: {self._volume_num} Author:" \
                        f" {self._artist}"
        base_details = super().__str__()
        return '\n'.join([seperator, base_details, manga_details, seperator])


class Game(LibraryItem):

    def __init__(self, dev_studio, platform="PC", num_players=1, **kwargs):
        """
        :param dev_studio: a String, name of the game studio
        :param num_players: an int, max number of players
        :param kwargs: Any additional keyword attributes for the base
                       class. Required to have 'title' and 'call_num'.
        :precondition call_num: Call number must follow the format
                                G.###.###.### where # is a number.
        """
        call_num = kwargs["call_num"]
        if call_num[0:2] == "G." and call_num[2:5].isdigit() and \
                call_num[6:9].isdigit() and call_num[10:13].isdigit() and \
                call_num[5] == "." and call_num[9] == "." and \
                len(call_num) == 13:
            super().__init__(**kwargs)
            self._dev_studio = dev_studio
            self._platform = platform
            self._num_players = num_players
        else:
            raise InvalidCallNumberError(call_num)

    def __str__(self):
        seperator = "-" * 20
        game_details = f"Type: Game, Studio: {self._dev_studio}, Platform:" \
                       f"{self._platform}, Max Players: {self._num_players}"
        base_details = super().__str__()
        return '\n'.join([seperator, base_details, game_details, seperator])


class Movie(LibraryItem):

    def __init__(self, genre, release_year, **kwargs):
        """
        :param genre: a String
        :param release_year: a String
        :param kwargs: Any additional keyword attributes for the base
                       class. Required to have 'title' and 'call_num'.
        :precondition call_num: Call number must follow the format
                                M.###.###.### where # is a number.
        """
        call_num = kwargs["call_num"]
        if call_num[0:2] == "M." and call_num[2:5].isdigit() and \
                call_num[6:9].isdigit() and call_num[10:13].isdigit() and \
                call_num[5] == "." and call_num[9] == "." and \
                len(call_num) == 13:
            super().__init__(**kwargs)
            self._genre = genre
            self._release_year = release_year
        else:
            raise InvalidCallNumberError(call_num)

    def __str__(self):
        seperator = "-" * 20
        movie_details = f"Type: Movie, Genre: {self._genre}, Release Year:" \
                        f" {self._release_year}"
        base_details = super().__str__()
        return '\n'.join([seperator, base_details, movie_details, seperator])


if __name__ == "__main__":
    # code to test classes.
    manga = Manga(title="Yotsuba!", call_num="MG.123.324.999",
                  num_copies=10, artist="Azuma Kiyohiko", volume_num=1)
    game = Game(title="Warcraft 3: Reign of Chaos", num_copies=4,
                call_num="G.001.234.876", dev_studio="Blizzard")
    movie = Movie(title="Jurassic Park", call_num="M.001.323.123",
                  num_copies=5, genre="Action/Adventure", release_year="1993")
    print(manga)
    print(game)
    print(movie)
