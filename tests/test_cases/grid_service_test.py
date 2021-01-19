import json

from model.grid import Grid
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class GridServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.gridSer = self.factory.get_grid_service()
        with open('../data/grid.json') as f:
            self.grid = Grid(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.gridSer.find(self.grid))

    def test_find_all(self):
        self.assertIsNotNone(self.gridSer.find_all(offset, pageSize, filters, sortBy))

    def test_create(self):
        self.assertIsNotNone(self.gridSer.create(self.grid))

    def test_update(self):
        self.assertIsNotNone(self.gridSer.update(self.grid))

    def test_create_form(self):
        self.assertIsNotNone(self.gridSer.create_form(self.grid))
