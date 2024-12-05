import unittest
from data import KaggleHubLoadData
from linear_regression import LinearRegressionBostonHouse
from sklearn.linear_model import LinearRegression


class TestLinelRegresion(unittest.TestCase):

    def setUp(self):
        self.df = KaggleHubLoadData(
            "arunjangir245/boston-housing-dataset",
            "BostonHousing.csv",
        ).read_dataset()

    def test_ckeck_model(self):
        ols = LinearRegressionBostonHouse()._ols
        self.assertIsInstance(ols, LinearRegression)
