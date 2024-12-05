import kagglehub
import pandas as pd


class KaggleHubLoadData:

    def __init__(self, repository, dataset_name):
        self.repository = repository
        self.dataset_name = dataset_name

    def read_dataset(self):
        dataset_path = self.dataset_download()
        dataset_name = dataset_path + "/" + self.dataset_name

        self.data = pd.read_csv(dataset_name)

        return self.data

    def dataset_download(self):
        path = kagglehub.dataset_download(
            self.repository)

        return path
