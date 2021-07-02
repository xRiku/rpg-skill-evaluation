import pandas as pd

class Evaluator:
    def __init__(self, dataset=None):
        if dataset is not None:
            self.df = pd.read_csv(dataset, usecols=["skill", "backward_text"])

    def load_dataset(self, dataset):
        self.df = pd.read_csv(dataset, usecols=["skill", "backward_text"])