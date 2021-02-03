import json
import os

from business.exception.business_error import BusinessError
from model.form import Form
from model.relation import Relation
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RelationServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        RELATION = os.path.join(self.TEST_CASES, '../data/relation.json')
        self.relationSer = self.factory.get_relation_service()
        with open(RELATION) as f:
            self.relation = Relation(json.load(f))
        FORM = os.path.join(self.TEST_CASES, '../data/form.json')
        with open(FORM) as f:
            self.form = Form(json.load(f))

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
        # With filters
        relations=self.relationSer.find_all('[{ "from": { "operator": "=", "values": 42 }" }]',
                                                       '[["type", "asc"]]')
        self.assertEqual(7, len(relations))

    def test_update_form(self):
        # TODO: 404 not found
        self.assertIsNotNone(self.relationSer.update_form(self.relation, self.form))

    def test_find_by_context(self):
        # TODO: Object not suscriptable
        self.assertIsNotNone(self.relationSer.find_by_context(str(self.relation._links["self"]["href"])))
