import json

from business.exception.business_error import BusinessError
from model.user import User
from model.work_package import WorkPackage
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class WorkPackageServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.wpSer = self.factory.get_work_package_service()
        with open('../data/work_package.json') as f:
            self.work_package = WorkPackage(json.load(f))
        with open('../data/relation.json') as f:
            self.relation = WorkPackage(json.load(f))
        with open('../data/user.json') as f:
            self.watcher = User(json.load(f))
        with open('../data/activity.json') as f:
            #     self.activity = WorkPackage(json.load(f))
            # with open('../data/schema.json') as f:
            self.schema = WorkPackage(json.load(f))
        with open('../data/attachment.json') as f:
            self.attachment = WorkPackage(json.load(f))

    # TODO
    def test_find_by_context(self):
        self.assertIsNotNone(self.wpSer.find_by_context(self.work_package["_links"]["self"]["href"]))

    # TODO
    def test_find_attachments(self):
        self.assertIsNotNone(self.wpSer.find_attachments(self.work_package))

    # TODO
    def test_add_attachment(self):
        self.assertIsNotNone(self.wpSer.add_attachment(self.work_package, self.attachment))

    def test_not_found(self):
        # There's no activity --> Exception
        with self.assertRaises(BusinessError):
            self.wpSer.find(self.work_package)

    def test_find(self):
        # TODO: We need a way to create a work package in order to change it
        current = self.wpSer.create(self.work_package)
        self.assertIsNotNone(self.wpSer.find(current))

    def test_update(self):
        # Without notify
        self.assertIsNotNone(self.wpSer.update(self.work_package))
        # With notify to false
        self.assertIsNotNone(self.wpSer.update(self.work_package, False))

    def test_delete(self):
        self.assertIsNotNone(self.wpSer.delete(self.work_package))

    # TODO
    # def test_find_schema(self):
    #     self.assertIsNotNone(self.wpSer.find_schema(self.schema))

    def test_find_all_schemas(self):
        self.assertIsNotNone(self.wpSer.find_all_schemas('[{ "id": { "operator": "=", "values": ["12-1", "14-2"] } }]'))

    def test_update_work_package_form(self):
        self.assertIsNotNone(self.wpSer.update_work_package(self.work_package))

    def test_find_all(self):
        work_packages = self.wpSer.find_all(25, 25, '[{ "type_id": { "operator": "=", "values": ["1", "2"] }}]',
                                            '[["status", "asc"]]', "status", True)

    def test_create(self):
        # Without notify
        self.assertIsNotNone(self.wpSer.create(self.work_package))
        # With notify to false
        self.assertIsNotNone(self.wpSer.create(self.work_package, False))

    # TODO
    def test_create_form(self):
        self.assertIsNotNone(self.wpSer.create_form(self.work_package))

    # TODO
    def test_create_relation(self):

        self.assertIsNotNone(self.wpSer.create_relation(self.work_package, self.relation))

    def test_find_relations(self):
        self.assertIsNotNone(self.wpSer.find_relations(self.work_package))

    def test_create_relation_form(self):
        self.assertIsNotNone(self.wpSer.create_relation_form(self.relation))

    def test_find_watchers(self):
        self.assertIsNotNone(self.wpSer.find_watchers(self.work_package))

    def test_create_watcher(self):
        self.assertIsNotNone(self.wpSer.create_watcher(self.work_package, self.watcher))

    def test_delete_watcher(self):
        self.assertIsNotNone(self.wpSer.delete_watcher(self.work_package, self.watcher))

    def test_find_relation_candidates(self):
        relations=self.wpSer.find_relation_candidates(self.work_package,
                            [Filter("status_id", "o", "null")], "rollout", "follows", 25)
        self.assertEqual(0, len(relations))

    def test_find_available_watchers(self):
        self.assertIsNotNone(self.wpSer.find_available_watchers(self.work_package))

    def test_find_available_projects(self):
        self.assertIsNotNone(self.wpSer.find_available_projects(self.work_package))

    def test_find_revisions(self):
        self.assertIsNotNone(self.wpSer.find_revisions(self.work_package))

    def test_find_activities(self):
        self.assertIsNotNone(self.wpSer.find_activities(self.work_package))

    def test_create_activity(self):
        self.assertIsNotNone(self.wpSer.create_activity(self.work_package, self.activity))
        self.assertIsNotNone(self.wpSer.create_activity(self.work_package, self.activity, False))

