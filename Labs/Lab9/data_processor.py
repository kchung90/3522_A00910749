from pandas import read_excel


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
        print(labels)
        print(title)
        print(data)

        for callback in self.callbacks:
            callback(title, data, labels, output_title)
