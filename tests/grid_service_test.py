import json
import unittest

from business.services.grid_service import GridService


class GridServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.gridSer = GridService()
        self.grid = json.loads('/data/grid.json')

    def test_find(self):
        self.assertNotNull(self.gridSer.find(grid))

    def test_find_all(self):
        self.assertNotNull(self.gridSer.find_all(offset, pageSize, filters, sortBy))

    def test_create(self):
        self.assertNotNull(self.gridSer.create(self.grid))

    def test_update(self):
        self.assertNotNull(self.gridSer.update(self.grid))

    def test_create_form(self):
        self.assertNotNull(self.gridSer.create_form(self.grid))
