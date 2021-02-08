import json
import os

from model.form import Form
from model.grid import Grid
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class GridServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/grid.json')
        self.gridSer = self.factory.get_grid_service()
        with open(DATA) as f:
            self.grid = Grid(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.gridSer.find(self.grid))

    # TODO: FIX ME: urn:openproject-org:api:v3:errors:InvalidQuery","message":["Filters Page does not exist."]
    def test_find_all_with_filters(self):
        grids = self.gridSer.find_all(25, 25, [Filter("page", "=", ["/my/page"])], sort_by=None)
        self.assertEqual(0, len(grids))

    def test_find_all(self):
        grids = self.gridSer.find_all()
        self.assertEqual(4, len(grids))

    def test_create(self):
        #  TODO: FIXME:{"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:InvalidRequestBody",
        #  "message":"The request could not be parsed as JSON.","_embedded":{"details":{"parseError":"unexpected character (after ) at line 1, column 1"}}}
        DATA = os.path.join(self.TEST_CASES, '../data/inputs/grid.json')
        with open(DATA) as f:
            g = Grid(json.load(f))
        g = self.gridSer.create(g)
        self.assertEqual(g.widgets[0].identifier, self.gridSer.find(g).widgets[0].identifier)

    def test_update(self):
        # TODO: To test
        self.assertIsNotNone(self.gridSer.update(self.grid))

    def test_create_form(self):
        # TODO: To test
        with open(os.path.join(self.TEST_CASES, '../data/inputs/grid.json')) as f:
            grid_form = Form(json.load(f))
        self.assertIsNotNone(self.gridSer.create_form(grid_form))

    def test_update_form(self):
        # TODO: To test
        with open(os.path.join(self.TEST_CASES, '../data/inputs/grid.json')) as f:
            grid_form = Form(json.load(f))
        self.assertIsNotNone(self.gridSer.update_form(self.grid, grid_form))
