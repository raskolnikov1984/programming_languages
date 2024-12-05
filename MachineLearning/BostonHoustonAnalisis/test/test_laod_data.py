import unittest
from typing import Callable
from data import KaggleHubLoadData
import pandas as pd


class TestData(unittest.TestCase):

    def setUp(self):
        self.dataset_name = "BostonHousing.csv"
        self.repository = "arunjangir245/boston-housing-dataset"

    def test_load_data(self):
        data = KaggleHubLoadData(
            self.repository, self.dataset_name).read_dataset()
        expected_columns = [
            'crim', 'zn', 'indus', 'chas', 'nox',
            'rm', 'age', 'dis', 'rad',
            'tax', 'ptratio', 'b', 'lstat', 'medv'
        ]
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(expected_columns, data.columns.to_list())
