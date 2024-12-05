from data import KaggleHubLoadData

if __name__ == '__main__':
    dataset_name = "BostonHousing.csv"
    repository = "arunjangir245/boston-housing-dataset"

    loader = KaggleHubLoadData(repository, dataset_name)
    data = loader.read_dataset()
