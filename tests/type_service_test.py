import unittest

from business.type_service import TypeService


class TypeServiceTestCase(unittest.TestCase):
    typeSer = TypeService()

    def test_find_all(self):
        return typeSer.find_all()


    def test_find(self):
        return typeSer.find(type)
