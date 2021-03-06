"""
@author Kevin Chung

This module acts as a proxy of a movie database.
"""
from Labs.Lab10.movie_database import Movie, MovieDatabase
from enum import Enum


class UserAccessEnum(Enum):
    """
    Represents access level of a user.
    """
    MEMBER = 0
    ADMIN = 1


class DuplicateEntryError(Exception):
    """
    Represents an exception that is raised when a duplicated data entry
    is found in the database.
    """
    def __init__(self):
        super().__init__("[WARNING] Duplicate entries are not allowed.")


class AccessLevelError(Exception):
    """
    Represents an exception that is raised when the user does not have
    permission to perform a task.
    """
    def __init__(self, task):
        super().__init__(f"[WARNING] MEMBER access level is not allowed to"
                         f" {task}")


class MovieDatabaseProxy:
    """
    Represents a wrapper class of a movie database. Fetches information
    from the movie database and stores in its cache.
    """

    def __init__(self, access_level, db_file_name: str, movies: list = None):
        """
        Initializes a MovieDatabaseProxy object.
        :param access_level: access level of a user as a UserAccessLevel
                             Enum
        :param db_file_name: a string, path to the database file ending
                             in extension .db.
        :param movies: a List containing objects of type Movie.
        """
        self.movie_db = MovieDatabase(db_file_name, movies)
        self.access_level = access_level
        self.cache = []
        self.update_cache()

    def update_cache(self):
        """
        Fetches information from its database and store information in
        the cache
        """
        for movie in [db_movie for db_movie in self.movie_db.view()]:
            self.cache.append(movie)

    def connect(self):
        """
        Establishes a connection to the database and instantiates the
        cursor as well. If the movies table or the file does not exist,
        it creates one.
        """
        self.movie_db.connect()

    def close_connection(self):
        """
        Closes the connection to the database preventing further
        changes.
        """
        self.movie_db.close_connection()

    def insert(self, movie: Movie):
        """
        Inserts a row into the movies database. Refer to the column
        headings in the MovieDatabase class comments to see what the
        movies database is composed of. Cache is updated after the
        movie is inserted into the database.
        :param movie: a Movie object
        """
        movie_list_db = [db_movie for db_movie in self.movie_db.view()]
        if self.access_level == UserAccessEnum.ADMIN:
            if not movie_list_db:
                inserted_movie = self.movie_db.insert(movie)
                self.cache.append(inserted_movie)
            else:
                for movie_in_db in movie_list_db:
                    if movie.title == movie_in_db.title and \
                            movie.director == movie_in_db.director and \
                            movie.release_year == movie_in_db.release_year \
                            and movie.language == movie_in_db.language:
                        raise DuplicateEntryError

                inserted_movie = self.movie_db.insert(movie)
                self.cache.append(inserted_movie)
        else:
            raise AccessLevelError("insert")

    def view(self) -> list:
        """
        Retrieves all the rows in the cache and movie database.
        """
        movie_list = ["Movies in Cache" + ("-" * 50)]
        for movie in self.cache:
            movie_list.append(movie)
        movie_list.append("Movies in Database" + ("-" * 47))

        db_movie_list = self.movie_db.view()
        for movie in db_movie_list:
            movie_list.append(movie)

        return movie_list

    def delete(self, movie_id):
        """
        Deletes a row specified by the key in the movies table. Removes
        a Movie object with the same movie_id from the cache.
        :param movie_id: an int
        """
        if self.access_level == UserAccessEnum.ADMIN:
            self.movie_db.delete(movie_id)
            for cache_movie in self.cache:
                if cache_movie.key == movie_id:
                    print(f"Movie: '{cache_movie.title}' was deleted")
                    self.cache.remove(cache_movie)
        else:
            raise AccessLevelError("delete")

    def search(self, title="", director="", language="", release_year=""):
        """
        Searches the cache to return a list of movies that match any
        combination of the given parameters. If not found, then
        searches the database to retrieves the rows that match any
        combination of the given parameters.
        :param title: a string
        :param director: a string
        :param language: a string, ISO language code
        :param release_year: an int
        :return: list of movies
        """
        movie_list = []
        print("Querying Cache" + ("-" * 50))
        for movie in self.cache:
            if title == movie.title or \
                    director == movie.director or \
                    language == movie.language or \
                    int(release_year) == movie.release_year:
                movie_list.append(movie)

        if not movie_list:
            print("Querying Database" + ("-" * 47))
            movie_list = self.movie_db.search(
                title, director, language, release_year)

        try:
            for movie in movie_list:
                if movie not in [cache_movie for cache_movie in self.cache]:
                    self.cache.append(movie)
        finally:
            return movie_list


def main():
    """
    Drives the program.
    """
    proxy_admin = MovieDatabaseProxy(UserAccessEnum.ADMIN, "movies.db")
    proxy_member = MovieDatabaseProxy(UserAccessEnum.MEMBER, "movies.db")

    try:
        print("-" * 100)
        print("Inserting a movie:\n")
        # Member inserting a movie - should raise error
        # proxy_member.insert(Movie("Titanic", "James Cameron", 1997, "ENG"))

        # Admin inserting movies
        proxy_admin.insert(Movie("Titanic", "James Cameron", 1997, "ENG"))
        proxy_admin.insert(Movie("Avatar", "James Cameron", 2009, "ENG"))
        proxy_admin.insert(Movie("Terminator", "James Cameron", 1984, "ENG"))
        print("\n")

        print("-" * 100)
        print("Deleting a movie:\n")
        # Member deleting a movie - should raise error
        # proxy_member.delete(1)

        # Admin deleting a movie
        proxy_admin.delete(1)
        print("\n")

        print("-" * 100)
        print("Searching for a movie:\n")
        # Admin searching for movies with director "James Cameron"
        for movie in proxy_admin.search(director="James Cameron"):
            print(movie)
        # Member searching for movies released in 2009
        for movie in proxy_member.search(release_year="2009"):
            print(movie)
        print("\n")

        print("-" * 100)
        print("Viewing Movies in Cache and Database:\n")
        print("Movies in Admin Proxy:")
        for movie in proxy_admin.view():
            print(movie)
        print("\nMovies in Member Proxy:")
        for movie in proxy_member.view():
            print(movie)

    except AccessLevelError as e:
        print(e)
    except DuplicateEntryError as e:
        print(e)


if __name__ == '__main__':
    main()
