import json

from business.exception.business_error import BusinessError
from model.relation import Relation
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RelationServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.relationSer = self.factory.get_relation_service()
        with open('../data/relation.json') as f:
            self.relation = Relation(json.load(f))

    def test_find(self):
        # There's no relation --> Exception
        with self.assertRaises(BusinessError):
            self.assertIsNotNone(self.relationSer.find(self.relation))

    def test_update(self):
        #TODO: create relation before
        self.assertIsNotNone(self.relationSer.update(self.relation))

    def test_delete(self):
        #TODO: create relation before
        self.assertIsNotNone(self.relationSer.delete(self.relation))

    def test_find_schema(self):
        #TODO:  {"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:BadRequest","message":"Bad request: id is invalid"}
        self.assertIsNotNone(self.relationSer.find_schema())

    def test_find_all(self):
        output=self.relationSer.find_all('[{ "from": { "operator": "=", "values": 42 }" }]',
                                                       '[["type", "asc"]]')
        print(output)

    def test_update_form(self):
        self.assertIsNotNone(self.relationSer.update_form(self.relation))

    def find_by_context(self):
        self.assertIsNotNone(self.relationSer.find_by_context(context))
