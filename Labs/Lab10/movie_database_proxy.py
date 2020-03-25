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
        pass

    def close_connection(self):
        pass

    def insert(self, movie: Movie):
        pass

    def view(self) -> list:
        pass

    def delete(self, movie_id):
        pass

    def search(self, title="", director="", language="", release_year=""):
        pass
