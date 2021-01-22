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

    # TODO: Filters are running well?
    def test_find_all_with_filters(self):
        grids = self.gridSer.find_all(25, 25, '[{ "page": { "operator": "=", "values": ["/my/page"] } }]', sort_by=None)
        self.assertEqual(0, len(grids))

    def test_find_all(self):
        grids = self.gridSer.find_all()
        self.assertEqual(4, len(grids))

    def test_create(self):
        # TODO: b'{"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError",
        #  "message":"An internal error has occured. string not matched"}'
        with open('../data/grid_create.json') as f:
            g = Grid(json.load(f))
        g = self.gridSer.create(g)
        self.assertEqual(g.widgets[0].identifier, self.gridSer.find(g).widgets[0].identifier)

    def test_update(self):
        # TODO: To test
        self.assertIsNotNone(self.gridSer.update(self.grid))

    def test_create_form(self):
        # TODO: To test
        self.assertIsNotNone(self.gridSer.create_form(self.grid))
