import argparse


class Request:

    def __init__(self, mode, input_data, expanded, input_file=None,
                 output_file=None):
        self.mode = mode
        self.input_data = input_data
        self.expanded = expanded
        if input_file:
            self.input_file = input_file
        else:
            self.input_file = None
        if output_file:
            self.output_file = output_file
        else:
            self.output_file = None

    @classmethod
    def commandline_request(cls):
        parser = argparse.ArgumentParser()

        parser.add_argument("mode", type=str,
                            choices=["pokemon", "ability", "move"],
                            help="Select the mode. Choices can be one of "
                                 "pokemon, ability, or move")

        input_group = parser.add_mutually_exclusive_group(required=True)
        input_group.add_argument("--inputfile", type=str,
                                 help="Name of a text file that will be used "
                                      "to query the Pokedex")
        input_group.add_argument("--inputdata", type=str,
                                 help="A Name or an ID that will be used to "
                                      "query the Pokedex")

        args = parser.parse_args()
        return args


def main():
    cmd_args = Request.commandline_request()
    print(cmd_args)


if __name__ == '__main__':
    main()
