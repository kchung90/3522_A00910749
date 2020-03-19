import abc
from matplotlib import pyplot as plt
from prettytable import PrettyTable


class IObserver:

    def __call__(self, title, data, labels, output_name):
        pass


class Graph(abc.ABC):

    @abc.abstractmethod
    def __call__(self, title, data, labels, output_name):
        pass


class LineGraph(Graph):

    def __init__(self, line_style, has_fill=False, fill_colour=None):
        self.line_style = line_style
        self.has_fill = has_fill
        self.fill_colour = fill_colour

    def __call__(self, title, data, labels, output_name):
        plt.title(title)
        if self.has_fill:
            plt.plot(data[0], data[1], self.line_style,
                     color=f"{self.fill_colour}")
        else:
            plt.plot(data[0], data[1], self.line_style)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        plt.savefig(f"{output_name}_line.png")


class BarGraph(Graph):

    def __init__(self, is_horizontal=False, edge_colour=None, bar_colour=None):
        self.is_horizontal = is_horizontal
        self.edge_colour = edge_colour
        self.bar_colour = bar_colour

    def __call__(self, title, data, labels, output_name):
        plt.title(title)
        if self.is_horizontal:
            plt.barh(data[0], data[1],
                     color=f"{self.bar_colour}",
                     edgecolor=f"{self.edge_colour}")
        else:
            plt.bar(data[0], data[1],
                    color=f"{self.bar_colour}",
                    edgecolor=f"{self.edge_colour}")
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        plt.savefig(f"{output_name}_bar.png")


class TableGenerator:

    def __init__(self, align=None):
        self.align = align

    def __call__(self, title, data, labels, output_name):
        x = PrettyTable()
        column_name = [labels[0], labels[1]]
        if self.align:
            x.align[labels[0]] = self.align
            x.align[labels[1]] = self.align
        x.add_column(column_name[0], data[0])
        x.add_column(column_name[1], data[1])
        table_txt = x.get_string(title=title)
        with open(f"{output_name}_table.txt", mode="w", encoding="utf-8") as\
                file:
            file.write(table_txt)
