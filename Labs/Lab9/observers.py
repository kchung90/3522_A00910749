import abc


class Observers:

    def __call__(self, title, data, labels, output_name):
        self.title = title
        self.data = []
        self.labels = []
        self.output_name = output_name


class Graph(abc.ABC):

    @abc.abstractmethod
    def __call__(self, title, data, labels, output_name):
        pass


class LineGraph(Graph):

    def __init__(self, line_style, has_fill, fill_colour):
        self.line_style = line_style
        self.has_fill = has_fill
        self.fill_colour = fill_colour

    def __call__(self, title, data, labels, output_name):
        self.title = title
        self.data = []
        self.labels = []
        self.output_name = output_name


class BarGraph(Graph):

    def __init__(self, is_horizontal, edge_colour, bar_colour):
        self.is_horizontal = is_horizontal
        self.edge_colour = edge_colour
        self.bar_colour = bar_colour

    def __call__(self, title, data, labels, output_name):
        self.title = title
        self.data = []
        self.labels = []
        self.output_name = output_name


class TableGenerator:

    def __init__(self, align):
        self.align = align

    def __call__(self, title, data, labels, output_name):
        self.title = title
        self.data = []
        self.labels = []
        self.output_name = output_name
