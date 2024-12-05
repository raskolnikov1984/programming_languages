#!/usr/bin/env python3
import unittest
from eda import BostonHouseEDA


class TestBostonHouseEDA(unittest.TestCase):

    def setUp(self):
        self.dataset_name = "BostonHousing.csv"
        self.repository = "arunjangir245/boston-housing-dataset"
        self._bh = BostonHouseEDA(
            self.repository, self.dataset_name)

    def test_split_dataset_training_testing(self):
        self._bh.split_dataset_training_testing()
        # raise Exception(self._bh.df.shape)
        df_shape_split = list(zip(self._bh.X_train.shape, self._bh.X_test.shape))
        X_shape = sum(df_shape_split[0])
        y_shape = sum(df_shape_split[1])
        self.assertEqual(X_shape, 506)
        self.assertEqual(y_shape, 26)

        # raise Exception(
        #     self._bh.X_train.shape, self._bh.X_test.shape, self._bh.y_train.shape, self._bh.y_train.shape)
