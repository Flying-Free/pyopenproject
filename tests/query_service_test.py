import unittest

from business.query_service import QueryService


class QueryServiceTestCase(unittest.TestCase):
    querySer = QueryService()

    def query_request(self):
        self.assertNotNull(self.querySer.request(1))
