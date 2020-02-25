class CustomDictionary:

    def __init__(self, path):
        with open(path, mode="r", encoding="utf-8") as my_file:

            lines = [line.split("\n") for line in
                     list(my_file.read().split("--"))]

            self.definitions = {value[0]: value[1:] for value in lines
                                if value != ['']}

            # self.words_queried

    def query(self, word):
        word_list = ""
        if word in self.definitions.keys():
            for definition in self.definitions[word]:
                word_list += definition
        return word_list

    def export(self):
        pass


def main():
    test = CustomDictionary("data.txt")
    print(test.query("rain"))


if __name__ == '__main__':
    main()
