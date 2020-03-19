class DataProcessor:

    def __init__(self):
        self.callbacks = []

    def subscribe_callbacks(self, *args):
        for arg in args:
            self.callbacks.append(arg)

    def process_data(self, excel_file, output_title):
        pass