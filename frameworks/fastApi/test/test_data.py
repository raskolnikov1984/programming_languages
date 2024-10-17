#!/usr/bin/env python3
import unittest
from ..main import load_json, add_element_json


class TestData(unittest.TestCase):

    def setUp(self):
        self.valid_json_file = 'movies.json'

    def test_load_valid_json(self):
        result = load_json('./data/'+self.valid_json_file)
        self.assertIsInstance(result, list)

    def test_add_element_json(self):
        new_element = {
            "id": 6,
            "title": "The Matrix Reload",
            "director": "Lana Wachowski, Lilly Wachowski",
            "release_year": 1999,
            "genre": "Action",
            "rating": 8.7
        }
        file_path = './data/example.json'
        current_elements = load_json(file_path)
        add_element_json(file_path, new_element)
        update_elements = load_json(file_path)

        self.assertGreater(len(update_elements), len(current_elements))




if __name__ == '__main__':
    unittest.main()
