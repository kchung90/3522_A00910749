"""
@author Kevin Chung

This module depicts the observers in the observer pattern. These
observers are callable objects and are called in the core to generate
graphs or tables.
"""
import abc
from matplotlib import pyplot as plt
from prettytable import PrettyTable


class Graph(abc.ABC):
    """
    An abstract class that represents objects that generate graphs when
    they are executed as functions.
    """

    @abc.abstractmethod
    def __call__(self, title, data, labels, output_name):
        """
        Allows the objects to be executed as functions. Needs to be
        overridden by subclasses.
        :param title: title of the graph as a String
        :param data: data for x-axis and y-axis as a List
        :param labels: labels for x-axis and y-axis as a List
        :param output_name: name of the output file as a String
        """
        pass


class LineGraph(Graph):
    """
    Represents an object that generates a line graph when it is called
    and executed as a function
    """

    def __init__(self, line_style, has_fill=False, fill_colour=None):
        """
        Initializes a LineGraph object
        :param line_style: style of a line in a line graph as a String
        :param has_fill: tells if a line graph has a fill as a Bool
        :param fill_colour: colour of the fill as a String
        """
        self.line_style = line_style
        self.has_fill = has_fill
        self.fill_colour = fill_colour

    def __call__(self, title, data, labels, output_name):
        """
        Allows the object to be executed as a function. Generates a
        line graph when executed.
        :param title: title of the graph as a String
        :param data: data for x-axis and y-axis as a List
        :param labels: labels for x-axis and y-axis as a List
        :param output_name: name of the output file as a String
        """
        plt.title(title)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        if self.has_fill:
            plt.plot(data[0], data[1], self.line_style)
            plt.fill_between(data[0], data[1], color=f"{self.fill_colour}")
        else:
            plt.plot(data[0], data[1], self.line_style)
        plt.savefig(f"{output_name}_line.png")
        plt.clf()


class BarGraph(Graph):
    """
    Represents an object that generates a bar graph when it is called
    and executed as a function
    """
    def __init__(self, edge_colour, bar_colour, is_horizontal=False):
        """
        Initializes a BarGraph object
        :param edge_colour: colour of the edge of the bar as a String
        :param bar_colour: colour of the bar in a bar graph as a String
        :param is_horizontal: tells if a graph is a horizontal graph as
        a Bool
        """
        self.is_horizontal = is_horizontal
        self.edge_colour = edge_colour
        self.bar_colour = bar_colour

    def __call__(self, title, data, labels, output_name):
        """
        Allows the object to be executed as a function. Generates a
        vertical bar graph or a horizontal bar graph when executed.
        :param title: title of the graph as a String
        :param data: data for x-axis and y-axis as a List
        :param labels: labels for x-axis and y-axis as a List
        :param output_name: name of the output file as a String
        """
        plt.title(title)
        if self.is_horizontal:
            plt.xlabel(labels[1])
            plt.ylabel(labels[0])
            plt.barh(data[0], data[1],
                     color=f"{self.bar_colour}",
                     edgecolor=f"{self.edge_colour}")
        else:
            plt.xlabel(labels[0])
            plt.ylabel(labels[1])
            plt.bar(data[0], data[1],
                    color=f"{self.bar_colour}",
                    edgecolor=f"{self.edge_colour}")
        plt.savefig(f"{output_name}_bar.png")
        plt.clf()


class TableGenerator:
    """
    Represents an object that generates a table when it is called
    and executed as a function
    """

    def __init__(self, align=None):
        """
        Initializes a TableGenerator object
        :param align: alignment of data in a column as a String
        """
        self.align = align

    def __call__(self, title, data, labels, output_name):
        """
        Allows the object to be executed as a function. Generates a
        table when executed.
        :param title: title of the table as a String
        :param data: data for two columns as a List
        :param labels: labels for columns as a List
        :param output_name: name of the output file as a String
        """
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
