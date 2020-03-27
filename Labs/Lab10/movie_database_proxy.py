from Labs.Lab10.movie_database import Movie, MovieDatabase
from enum import Enum


class UserAccessEnum(Enum):
    MEMBER = 0
    ADMIN = 1


class AccessLevelError(Exception):
    def __init__(self, task):
        super().__init__(f"MEMBER access level is not allowed to {task}")


class MovieDatabaseProxy:

    def __init__(self, access_level, db_file_name: str, movies: list = None):
        self.movie_db = MovieDatabase(db_file_name, movies)
        self.access_level = access_level
        self.cache = []
        self.update_cache()

    def update_cache(self):
        db_movie_list = self.movie_db.view()
        for movie in db_movie_list:
            self.cache.append(movie)

    def connect(self):
        self.movie_db.connect()

    def close_connection(self):
        self.movie_db.close_connection()

    def insert(self, movie: Movie):
        if self.access_level == UserAccessEnum.ADMIN:
            self.movie_db.insert(movie)
            self.cache.append(movie)
        else:
            raise AccessLevelError("insert")

    def view(self) -> list:
        movie_list = ["--- Movies in Cache:"]
        for movie in self.cache:
            movie_list.append(movie)
        movie_list.append("--- Movies in the Database:")

        db_movie_list = self.movie_db.view()
        for movie in db_movie_list:
            movie_list.append(movie)

        return movie_list

    def delete(self, movie_id):
        if self.access_level == UserAccessEnum.ADMIN:
            self.movie_db.delete(movie_id)
            for cache_movie in self.cache:
                if cache_movie.key == movie_id:
                    self.cache.remove(cache_movie)
        else:
            raise AccessLevelError("delete")

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
                if movie not in [cache_movie for cache_movie in self.cache]:
                    self.cache.append(movie)
        finally:
            return movie_list


def main():
    # movie_list = [Movie("title1", "director1", 2020, "ENG"),
    #               Movie("title2", "director2", 2019, "FR"),
    #               Movie("title3", "director3", 2018, "ENG"),
    #               Movie("title4", "director1", 2020, "KR"),
    #               Movie("title5", "director2", 2018, "FR")]
    movie_list = []
    proxy1 = MovieDatabaseProxy(UserAccessEnum.ADMIN, "movie.db", movie_list)
    # for movie in proxy1.search(language="FR"):
    #     print(movie)
    #
    # for movie in proxy1.search(language="FR"):
    #     print(movie)
    #
    # for movie in proxy1.search("", "", "ENG"):
    #     print(movie)
    #
    # print("\n\n\n cache list")
    # for a in proxy1.cache:
    #     print(a)
    # for movie in proxy1.view():
    #     print(movie)

    # try:
    #     proxy1.insert(Movie("test", "test_director", 2020, "ENG"))
    # except AccessLevelError as e:
    #     print(e)

    try:
        proxy1.delete(4)
    except AccessLevelError as e:
        print(e)

    for movie in proxy1.cache:
        print(movie)
    #
    # for movie in proxy1.view():
    #     print(movie)


if __name__ == '__main__':
    main()
