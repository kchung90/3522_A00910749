from Labs.Lab10.movie_database import Movie, MovieDatabase
from enum import Enum


class UserAccessEnum(Enum):
    MEMBER = 0
    ADMIN = 1


class MovieDatabaseProxy:

    def __init__(self, access_level, db_file_name: str, movies: list = None):
        self.movie_db = MovieDatabase(db_file_name, movies)
        self.access_level = access_level
        self.cache = []

    def connect(self):
        self.movie_db.connect()

    def close_connection(self):
        self.movie_db.close_connection()

    def insert(self, movie: Movie):
        pass

    def view(self) -> list:
        pass

    def delete(self, movie_id):
        pass

    def search(self, title="", director="", language="", release_year=""):
        movie_list = []
        print("---------------Querying Cache---------------")
        for movie in self.cache:
            if title == movie.title or \
                    director == movie.director or \
                    language == movie.language or \
                    release_year == movie.release_year:
                movie_list.append(movie)

        if not movie_list:
            print("---------------Querying Database---------------")
            movie_list = self.movie_db.search(
                title, director, language, release_year)

        try:
            for movie in movie_list:
                self.cache.append(movie)
        finally:
            return movie_list
