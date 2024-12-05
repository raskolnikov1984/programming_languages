from data import KaggleHubLoadData

from sklearn.model_selection import train_test_split


class BostonHouseEDA:

    def __init__(self, repository, dataset_name):
        self.df = KaggleHubLoadData(
            repository, dataset_name).read_dataset()
        self.X = self.df.drop('medv', axis=1)
        self.y = self.df['medv']

    def split_dataset_training_testing(self):
        self.X_train, self.X_test, self.y_train, self.y_test =\
            train_test_split(
                self.X, self.y, test_size=0.2, random_state=42)
