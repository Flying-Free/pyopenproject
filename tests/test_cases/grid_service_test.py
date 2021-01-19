import json
import unittest

from business.service_factory import ServiceFactory
from model.grid import Grid


class GridServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.gridSer = ServiceFactory.get_grid_service()
        with open('../data/grid.json') as f:
            self.grid = Grid(json.load(f))

    def test_find(self):
        self.assertNotNull(self.gridSer.find(self.grid))

    def test_find_all(self):
        self.assertNotNull(self.gridSer.find_all(offset, pageSize, filters, sortBy))

    def test_create(self):
        self.assertNotNull(self.gridSer.create(self.grid))

    def test_update(self):
        self.assertNotNull(self.gridSer.update(self.grid))

    def test_create_form(self):
        self.assertNotNull(self.gridSer.create_form(self.grid))
