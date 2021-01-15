import json
import unittest

from business.exception.business_error import BusinessError
from business.service_factory import ServiceFactory
from model.work_package import WorkPackage


class WorkPackageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.wpSer = ServiceFactory.get_work_package_service()
        with open('./data/work_package.json') as f:
            self.work_package = WorkPackage(json.load(f))

    # TODO
    def test_find_by_context(self):
        self.assertIsNotNone(self.wpSer.find_by_context(context))

    # TODO
    def test_find_attachments(self):
        self.assertIsNotNone(self.wpSer.find_attachments(self.work_package))

    # TODO
    def test_add_attachment(self):
        self.assertIsNotNone(self.wpSer.add_attachment(self.work_package, attachment))

    def test_find(self):
        # There's no activity --> Exception
        with self.assertRaises(BusinessError):
            self.wpSer.find(self.work_package)

    def test_update(self):
        # Without notify
        self.assertIsNotNone(self.wpSer.update(self.work_package))
        # With notify to false
        self.assertIsNotNone(self.wpSer.update(self.work_package, False))

    def test_delete(self):
        self.assertIsNotNone(self.wpSer.delete(self.work_package))

    # TODO
    def test_find_schema(self):
        self.assertIsNotNone(self.wpSer.find_schema(schema))

    def test_find_all_schemas(self):
        self.assertIsNotNone(self.wpSer.find_all_schemas('[{ "id": { "operator": "=", "values": ["12-1", "14-2"] } }]'))

    def test_update_work_package_form(self):
        self.assertIsNotNone(self.wpSer.update_work_package(self.work_package))

    def test_find_all(self):
        self.assertIsNotNone(self.wpSer.find_all(25, 25,'[{ "type_id": { "operator": "=", "values": ["1", "2"] }}]', '[["status", "asc"]]', "status", True))

    def test_create(self):
        # Without notify
        self.assertIsNotNone(self.wpSer.create(self.work_package))
        # With notify to false
        self.assertIsNotNone(self.wpSer.create(self.work_package, False))

    # TODO
    def test_create_form(self):
        self.assertIsNotNone(self.wpSer.create_form(self.work_package))

    def test_create_relation(self):
        self.assertIsNotNone(self.wpSer.create_relation(self.work_package, relation))

    def test_find_relations(self):
        self.assertIsNotNone(self.wpSer.find_relations(self.work_package))

    def test_create_relation_form(self):
        self.assertIsNotNone(self.wpSer.create_relation_form(relation))

    def test_find_watchers(self):
        self.assertIsNotNone(self.wpSer.find_watchers(self.work_package))

    def test_create_watcher(self):
        self.assertIsNotNone(self.wpSer.create_watcher(self.work_package, watcher))

    def test_delete_watcher(self):
        self.assertIsNotNone(self.wpSer.delete_watcher(self.work_package, watcher))

    def test_find_relation_candidates(self):
        self.assertIsNotNone(self.wpSer.find_relation_candidates(self.work_package, filters, query, type, pageSize))

    def test_find_available_watchers(self):
        self.assertIsNotNone(self.wpSer.find_available_watchers(self.work_package))

    def test_find_available_projects(self):
        self.assertIsNotNone(self.wpSer.find_available_projects(self.work_package))

    def test_find_revisions(self, work_package):
        self.assertIsNotNone(self.wpSer.find_revisions(self.work_package))

    def test_find_activities(self):
        self.assertIsNotNone(self.wpSer.find_activities(self.work_package, notify))

    def test_create_activity(self):
        self.assertIsNotNone(self.wpSer.create_activity(self.work_package, activity, notify))
