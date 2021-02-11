import json
import os

from business.exception.business_error import BusinessError
from model.form import Form
from model.relation import Relation
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


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

    def test_not_found(self):
        # There's no relation --> Exception
        s = self.relationSer.find(self.relation)
        self.assertEqual(self.relation.type, s.type)
        self.assertEqual(self.relation.reverseType, s.reverseType)

    def test_operations(self):
        work_packages = self.factory.get_work_package_service().find_all()
        work_packages = list(filter(lambda x: x.__dict__["_links"]["status"]["title"] == "New", work_packages))
        f = work_packages[0]
        t = work_packages[1]
        relation = self.factory.get_work_package_service().create_relation(
            type="follows",
            work_package_from=f,
            work_package_to=t,
            description="Demo relation created using the API")
        self.assertEqual("Demo relation created using the API", relation.description)
        self.assertEqual("follows", relation.type)
        self.assertEqual("precedes", relation.reverseType)
        relation = self.factory.get_relation_service().update(Relation({
            "id": relation.id,
            "type": "blocks",
            "description": "Actually the supplier has to bend the steel before they can deliver it.",
            "delay": 3
        }))
        self.assertEqual("blocks", relation.type)
        self.assertEqual("Actually the supplier has to bend the steel before they can deliver it.",
                         relation.description)
        found_relation = self.relationSer.find(relation)
        self.assertEqual(relation.type, found_relation.type)
        self.factory.get_relation_service().delete(relation)
        with self.assertRaises(BusinessError):
            self.relationSer.find(relation)

    # FIXME: 404 Client Error: Not Found for url
    def test_find_schema(self):
        with self.assertRaises(BusinessError):
            self.relationSer.find_schema()
        s = self.relationSer.find_schema_by_type("follows")
        self.assertIsNotNone(s)

    # FIXME:
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError",
    #  "message":"An internal error has occured.
    #  PG::UndefinedColumn: ERROR:
    #  column \"type\" does not exist\nLINE 1: ...TRUE WHERE \"projects\".\"active\" = TRUE)))
    #  ORDER BY \"type\" ASC...\n                                                             ^\n"
    #  }
    def test_find_all(self):
        relations = self.relationSer.find_all()
        self.assertEqual(7, len(relations))
        # With filters
        relations = self.relationSer.find_all([Filter("involved", "=", ["42"])],
                                              '[["type", "asc"]]')
        self.assertEqual(7, len(relations))

    # FIXME: 404 Client Error: Not Found for url
    def test_update_form(self):
        work_packages = self.factory.get_work_package_service().find_all()
        work_packages = list(filter(lambda x: x.__dict__["_links"]["status"]["title"] == "New", work_packages))
        f = work_packages[0]
        t = work_packages[1]
        relation = self.factory.get_work_package_service().create_relation(
            type="follows",
            work_package_from=f,
            work_package_to=t,
            description="Demo relation created using the API")
        form = {
            "_type": "Relation",
            "type": "follows",
            "description": "let it rest for 3 days",
            "delay": 3
        }
        self.assertIsNotNone(self.relationSer.update_form(relation, form))
        self.factory.get_relation_service().delete(relation)
