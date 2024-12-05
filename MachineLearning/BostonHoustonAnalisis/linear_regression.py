from data import KaggleHubLoadData

from sklearn.linear_model import LinearRegression


class LinearRegressionBostonHouse:

    def __init__(self):
        self._ols = LinearRegression()
