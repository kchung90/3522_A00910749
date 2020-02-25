from difflib import get_close_matches


class CustomDictionary:

    def __init__(self, path):
        with open(path, mode="r", encoding="utf-8") as my_file:
            lines = [line.split("\n") for line in
                     list(my_file.read().split("--"))]

            self.definitions = {value[0]: value[1:] for value in lines
                                if value != ['']}

            # self.words_queried

    def query(self, word):
        word_lower_case = word.lower()
        word_checked = get_close_matches(word_lower_case,
                                         list(self.definitions.keys()))
        def_list = ""
        if word_checked[0] in self.definitions.keys():
            for definition in self.definitions[word_checked[0]]:
                def_list += definition + "\n"
        return def_list

    def export(self):
        pass


def main():
    test = CustomDictionary("data.txt")
    print(test.query("RAin"))


if __name__ == '__main__':
    main()
