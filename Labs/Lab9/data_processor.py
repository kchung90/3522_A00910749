from pandas import read_excel

from Labs.Lab9.observers import LineGraph, BarGraph, TableGenerator


class DataProcessor:

    def __init__(self):
        self.callbacks = []

    def subscribe_callbacks(self, *args):
        for arg in args:
            self.callbacks.append(arg)

    def process_data(self, excel_file, output_title):
        df = read_excel(excel_file)
        labels = df.columns.values.tolist()
        title = f"{labels[1]} vs {labels[0]}"
        data = []
        for label in labels:
            data.append(df[label].values.tolist())

        for callback in self.callbacks:
            callback(title, data, labels, output_title)


def main():
    dp = DataProcessor()
    line_graph = LineGraph("b-", True, "orange")
    bar_graph = BarGraph("black", "orange")
    tbl = TableGenerator("r")
    dp.subscribe_callbacks(bar_graph, line_graph, tbl)
    dp.process_data("Temperatures.xlsx", "temperature")


if __name__ == '__main__':
    main()
