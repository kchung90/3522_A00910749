"""
@author Kevin Chung

This module depicts the core in the observer pattern. DataProcessor
class reads an excel file and notifies all the observers subscribing
to it.
"""
from pandas import read_excel
from Labs.Lab9.observers import LineGraph, BarGraph, TableGenerator


class DataProcessor:
    """
    DataProcessor is responsible for reading an excel file and
    notifying its observers. It adds observers to list of callbacks and
    calls the observers to process the data.
    """

    def __init__(self):
        """
        initializes DataProcessor object.
        """
        self.callbacks = []

    def subscribe_callbacks(self, *args):
        """
        accepts variable number of callable objects and adds them to
        the list of callbacks
        :param args: callable IObserver objects
        """
        for arg in args:
            self.callbacks.append(arg)

    def process_data(self, excel_file, output_title):
        """
        reads an excel file and extracts data in two columns. Then
        passes data to objects in the list of callbacks to generate
        graphs or tables.
        :param excel_file: name of the excel file as a String
        :param output_title: title of the output file as a String
        """
        df = read_excel(excel_file)
        labels = df.columns.values.tolist()
        title = f"{labels[1]} vs {labels[0]}"
        data = []
        for label in labels:
            data.append(df[label].values.tolist())

        for callback in self.callbacks:
            callback(title, data, labels, output_title)


def main():
    """
    Drives the program.
    """
    dp = DataProcessor()
    line_graph = LineGraph("r-", True, "black")
    bar_graph = BarGraph("black", "green", False)
    tbl = TableGenerator("l")
    dp.subscribe_callbacks(bar_graph, line_graph, tbl)
    try:
        dp.process_data("Temperatures.xlsx", "temperature")
    except FileNotFoundError:
        print("File is not found. Please check the file name again.")


if __name__ == '__main__':
    main()
