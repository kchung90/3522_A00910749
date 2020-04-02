"""
@author Kevin Chung

This module accepts command line arguments from a user through the
terminal to create a Request object.
"""
import argparse


class Request:
    """
    Represents an object that stores data queried from a user using
    command line arguments
    """

    def __init__(self, mode: str, input_data: str, expanded: bool,
                 input_file: str = None, output_file: str = None):
        """
        Initializes the Request object
        :param mode: mode of the request as a str
        :param input_data: a name/id of the data to be queried as a str
        :param expanded: whether to send sub-queries as a bool
        :param input_file: name of an input file as a str
        :param output_file: name of an output file as a str
        """
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

    def __str__(self):
        """
        Returns the description of the Request object
        :return: description as a str
        """
        return f"Request:\n" \
               f"Mode: {self.mode}\n" \
               f"Input Data: {self.input_data}\n" \
               f"Expanded: {self.expanded}\n" \
               f"Input File: {self.input_file}\n" \
               f"Output File: {self.output_file}\n" \
               f"-------------------------------------------\n"

    @classmethod
    def commandline_request(cls):
        """
        Accepts user inputs from a terminal command line arguments and
        returns a Namespace
        :return: command line arguments as a Namespace
        """
        parser = argparse.ArgumentParser()

        parser.add_argument("mode", type=str,
                            choices=["pokemon", "ability", "move"],
                            help="Select the mode. Choices can be one of "
                                 "pokemon, ability, or move.")

        input_group = parser.add_mutually_exclusive_group(required=True)
        input_group.add_argument("--inputfile", type=str,
                                 help="Name of a text file that will be used "
                                      "to query the Pokedex.")
        input_group.add_argument("--inputdata", type=str,
                                 help="A Name or an ID that will be used to "
                                      "query the Pokedex.")

        parser.add_argument("-e", "--expanded", action="store_true",
                            help="When True, the Pokedex will do sub-queries "
                                 "to get more information about a particular "
                                 "attribute. Default is False.")

        parser.add_argument("-op", "--outputfile", type=str,
                            help="Name of an output text file that the "
                                 "results of all queries will be recorded.")

        args = parser.parse_args()
        return args


def main():
    """
    Drives the program.
    """
    cmd_args = Request.commandline_request()
    print(cmd_args)
    request = Request(mode=cmd_args.mode, input_data=cmd_args.inputdata,
                      expanded=cmd_args.expanded,
                      input_file=cmd_args.inputfile,
                      output_file=cmd_args.outputfile)
    print(request)


if __name__ == '__main__':
    main()
