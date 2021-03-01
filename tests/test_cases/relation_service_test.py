import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.util.filter import Filter
from pyopenproject.model.form import Form
from pyopenproject.model.relation import Relation
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RelationServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        RELATION = os.path.join(self.TEST_CASES, '../data/relation.json')
        self.relationSer = self.op.get_relation_service()
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
        # Find work packages
        work_packages = self.op.get_work_package_service().find_all()
        work_packages = list(filter(lambda x: x.__dict__["_links"]["status"]["title"] == "New", work_packages))
        f = work_packages[0]
        t = work_packages[1]
        # Find all relations without filters before create
        relations = self.relationSer.find_all()
        self.assertEqual(7, len(relations))
        # Create relation
        relation = self.op.get_work_package_service().create_relation(
            relation_type="follows",
            work_package_from=f,
            work_package_to=t,
            description="Demo relation created using the API")
        self.assertEqual("Demo relation created using the API", relation.description)
        self.assertEqual("follows", relation.type)
        self.assertEqual("precedes", relation.reverseType)
        # Update relation
        relation = self.op.get_relation_service().update(Relation({
            "id": relation.id,
            "type": "blocks",
            "description": "Actually the supplier has to bend the steel before they can deliver it.",
            "delay": 3
        }))
        self.assertEqual("blocks", relation.type)
        self.assertEqual("Actually the supplier has to bend the steel before they can deliver it.",
                         relation.description)
        # Find relation
        found_relation = self.relationSer.find(relation)
        self.assertEqual(relation.type, found_relation.type)
        # Find all relations without filters after create
        relations = self.relationSer.find_all()
        self.assertEqual(8, len(relations))
        # Find all with filters
        # TODO: type, name sortBy don't work
        relations = self.relationSer.find_all([Filter("involved", "=", ["42"])],
                                              '[["id", "asc"]]')
        self.assertEqual(0, len(relations))
        # Delete relation
        self.op.get_relation_service().delete(relation)
        with self.assertRaises(BusinessError):
            self.relationSer.find(relation)
        # Find all relations without filters after delete
        relations = self.relationSer.find_all()
        self.assertEqual(7, len(relations))

    # FIXME: 404 Client Error: Not Found for url
    def test_find_schema(self):
        with self.assertRaises(BusinessError):
            self.relationSer.find_schema()
        # s = self.relationSer.find_schema_by_type("follows")
        # self.assertIsNotNone(s)

    def test_update_form(self):
        work_packages = self.op.get_work_package_service().find_all()
        work_packages = list(filter(lambda x: x.__dict__["_links"]["status"]["title"] == "New", work_packages))
        f = work_packages[0]
        t = work_packages[1]
        relation = self.op.get_work_package_service().create_relation(
            relation_type="follows",
            work_package_from=f,
            work_package_to=t,
            description="Demo relation created using the API")
        # form = {
        #     "_type": "Relation",
        #     "type": "follows",
        #     "description": "let it rest for 3 days",
        #     "delay": 3
        # }
        # FIXME: 404 Client Error: Not Found for url
        # self.assertIsNotNone(self.relationSer.update_form(relation, form))
        self.op.get_relation_service().delete(relation)
