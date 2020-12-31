import unittest

from business.grid_service import GridService


class GridServiceTestCase(unittest.TestCase):
    gridSer = GridService()

    def grid_request(self):
        self.assertNotNull(self.gridSer.request(1))
