import unittest

from business.query_service import QueryService


class QueryServiceTestCase(unittest.TestCase):
    querySer = QueryService()

    def test_update(self, query):
        self.assertNotNull(self.querySer.update(query))

    def test_find(self, query, offset, pageSize, filters, columns, sortBy, groupBy, showSums, timelineVisible,
                     timelineLabels, timelineZoomLevel, highlightingMode, highlightedAttributes, showHierarchies):
        self.assertNotNull(self.querySer.find(query, offset, pageSize, filters, columns, sortBy, groupBy, showSums, timelineVisible,
                     timelineLabels, timelineZoomLevel, highlightingMode, highlightedAttributes, showHierarchies))

    def test_delete(self, query):
        self.assertNotNull(self.querySer.delete(query))

    def star(self, query):
        self.assertNotNull(self.querySer.star(query))

    def test_unstar(self, query):
        self.assertNotNull(self.querySer.unstar(query))

    def test_find_all(self, filters):
        self.assertNotNull(self.querySer.find_all(filters))

    def test_create(self, query):
        self.assertNotNull(self.querySer.create(query))

    def test_create_form(self, form):
        self.assertNotNull(self.querySer.create_form(form))

    def test_schema(self):
        self.assertNotNull(self.querySer.schema())
