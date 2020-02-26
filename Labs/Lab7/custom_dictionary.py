from difflib import get_close_matches


class CustomDictionary:

    def __init__(self, path):
        with open(path, mode="r", encoding="utf-8") as my_file:
            f = my_file.read()
            if "--" not in f:
                raise ImportError
            else:
                lines = [line.split("\n") for line in
                         list(f.split("--"))]
        self.definitions = {value[0]: value[1:] for value in lines
                            if value != [""]}
        self.words_queried = []

    def query(self, word):
        closest_word = get_close_matches(word.lower(),
                                         list(self.definitions.keys()))
        if not closest_word:
            try:
                raise WordNotFoundError(word)
            except WordNotFoundError as e:
                print(e)
        else:
            if closest_word[0] not in self.words_queried:
                self.words_queried.append(closest_word[0])
            result = ""
            for definition in self.definitions[closest_word[0]]:
                if definition != "":
                    result += definition + "\n"
            return result

    def export(self):
        with open("word_queries.txt", mode="w", encoding="utf-8") as my_file:
            for word in self.words_queried:
                my_file.write("--" + word + "\n")
                for definition in self.definitions[word]:
                    if definition != "":
                        my_file.write(definition + "\n")


class WordNotFoundError(Exception):

    def __init__(self, missing_word):
        self.missing_word = missing_word
        super().__init__(f"'{self.missing_word}' is not found in the file.")


def main():
    try:
        my_dict = CustomDictionary("data.txt")
    except FileNotFoundError:
        print("File is not found")
    except ImportError:
        print("File format is not correct.")
    else:
        my_dict.query("reservation")
        my_dict.query("rain")
        my_dict.query("ksdf234234")
        my_dict.query("zodiac")
        my_dict.query("rain")
        my_dict.export()


if __name__ == '__main__':
    main()
