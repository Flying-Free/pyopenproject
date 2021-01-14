import json
import unittest

from business.services.query_service import QueryService


class QueryServiceTestCase(unittest.TestCase):


    def setUp(self):
        self.querySer = QueryService()
        self.query = json.loads('/data/query.json')

    def test_update(self):
        self.assertNotNull(self.querySer.update(self.query))

    def test_find(self):
        self.assertNotNull(self.querySer.find(self.query, offset, pageSize, filters, columns, sortBy, groupBy, showSums, timelineVisible,
                     timelineLabels, timelineZoomLevel, highlightingMode, highlightedAttributes, showHierarchies))

    def test_delete(self):
        self.assertNotNull(self.querySer.delete(self.query))

    def test_star(self):
        self.assertNotNull(self.querySer.star(self.query))

    def test_unstar(self):
        self.assertNotNull(self.querySer.unstar(self.query))

    def test_find_all(self):
        self.assertNotNull(self.querySer.find_all(filters))

    def test_create(self):
        self.assertNotNull(self.querySer.create(self.query))

    def test_create_form(self):
        self.assertNotNull(self.querySer.create_form(form))

    def test_schema(self):
        self.assertNotNull(self.querySer.schema())
