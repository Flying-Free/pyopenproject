import json
import os

from pyopenproject.model.grid import Grid
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class GridServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/grid.json')
        self.gridSer = self.op.get_grid_service()
        with open(DATA) as f:
            self.grid = Grid(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.gridSer.find(self.grid))

    # TODO: FIXME: urn:openproject-org:api:v3:errors:InvalidQuery","message":["Filters Page does not exist."]
    def test_find_all_with_filters(self):
        # grids = self.gridSer.find_all(25, 25, [Filter("page", "=", ["/my/page"])], sort_by=None)
        # self.assertEqual(0, len(grids))
        pass

    def test_find_all(self):
        grids = self.gridSer.find_all()
        self.assertEqual(7, len(grids))

    # FIXME  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InvalidRequestBody",
    #  "message":"The request could not be parsed as JSON.",
    #  "_embedded":{"details":{"parseError":"unexpected character (after ) at line 1, column 1"}}
    #  }
    def test_create(self):
        g = Grid(self.gridSer.create_form()["_embedded"]["payload"])
        demo_widget = {
            "identifier": "time_entries_current_user",
            "startRow": 1,
            "endRow": 8,
            "startColumn": 1,
            "endColumn": 3
        }
        g.widgets.append(demo_widget)
        # g = self.gridSer.create(g)
        # self.assertEqual(g.widgets[0], self.gridSer.find(g).widgets[0])

    # FIXME
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError",
    #  "message":"An internal error has occured. 405 Not Allowed"
    #  }
    def test_update(self):
        demo_widget = {
            "identifier": "time_entries_current_user",
            "startRow": 1,
            "endRow": 8,
            "startColumn": 1,
            "endColumn": 3
        }
        grids = self.gridSer.find_all()
        grid = grids[0]
        grid.widgets.append(demo_widget)
        # grid = self.gridSer.update(grid)
        # self.assertEqual(demo_widget, grid.widgets[0])

    def test_create_form(self):
        expected = Grid({'rowCount': 4, 'columnCount': 5, 'options': {}, 'widgets': [], '_links': {'attachments': []}})
        grid = Grid(self.gridSer.create_form()["_embedded"]["payload"])
        self.assertEqual(expected.__dict__, grid.__dict__)

    def test_update_form(self):
        form = {
            "rowCount": 8,
            "columnCount": 5,
            "widgets": [
                {
                    "identifier": "time_entries_current_user",
                    "startRow": 1,
                    "endRow": 8,
                    "startColumn": 1,
                    "endColumn": 3
                },
                {
                    "identifier": "news",
                    "startRow": 3,
                    "endRow": 8,
                    "startColumn": 4,
                    "endColumn": 5
                },
                {
                    "identifier": "documents",
                    "startRow": 1,
                    "endRow": 3,
                    "startColumn": 3,
                    "endColumn": 6
                }
            ]
        }
        grid = list(filter(lambda x: x.id == 1, self.gridSer.find_all()))[0]
        self.gridSer.update_form(grid, form)
        new_grid = list(filter(lambda x: x.id == 1, self.gridSer.find_all()))[0]
        self.assertNotEqual(grid, new_grid)
