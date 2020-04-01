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

    def __str__(self):
        return f"Request:\n" \
               f"Mode: {self.mode}\n" \
               f"Input Data: {self.input_data}\n" \
               f"Expanded: {self.expanded}\n" \
               f"Input File: {self.input_file}\n" \
               f"Output File: {self.output_file}\n" \
               f"-------------------------------------------\n"

    @classmethod
    def commandline_request(cls):
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
    cmd_args = Request.commandline_request()
    print(cmd_args)
    request = Request(mode=cmd_args.mode, input_data=cmd_args.inputdata,
                      expanded=cmd_args.expanded,
                      input_file=cmd_args.inputfile,
                      output_file=cmd_args.outputfile)
    print(request)


if __name__ == '__main__':
    main()
