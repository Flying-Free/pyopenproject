import json
import unittest

from business.work_package_service import WorkPackageService


class WorkPackageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.wpSer = WorkPackageService()
        self.work_package = json.loads('/data/work_package.json')

    def test_find_by_context(self):
        self.assertNotNull(self.wpSer.find_by_context(context))

    def test_find_attachments(self):
        self.assertNotNull(self.wpSer.find_attachments(self.work_package))

    def test_add_attachment(self):
        self.assertNotNull(self.wpSer.add_attachment(self.work_package, attachment))

    def test_find(self):
        self.assertNotNull(self.wpSer.find(notify))

    def test_update_work_package(self):
        self.assertNotNull(self.wpSer.update_work_package(self.work_package, notify))

    def test_delete_work_package(self):
        self.assertNotNull(self.wpSer.delete_work_package(self.work_package, notify))

    def test_find_schema(self):
        self.assertNotNull(self.wpSer.find_schema(schema))

    def test_find_all_schemas(self, filters):
        self.assertNotNull(self.wpSer.find_all_schemas(filters))

    def test_update_work_package_form(self):
        self.assertNotNull(self.wpSer.update_work_package(self.work_package))

    def test_find_all(self):
        self.assertNotNull(self.wpSer.find_all(notify, offset, pageSize,filters, sortBy, groupBy, showSums))

    def test_create(self):
        self.assertNotNull(self.wpSer.create(self.work_package, notify))

    def test_create_form(self):
        self.assertNotNull(self.wpSer.create_form(self.work_package))


    def test_create_relation(self):
        self.assertNotNull(self.wpSer.create_relation(self.work_package, relation))

    def test_find_relations_by_work_package(self):
        self.assertNotNull(self.wpSer.find_relations_by_work_package(self.work_package))

    def test_create_relation_form(self):
        self.assertNotNull(self.wpSer.create_relation_form(relation))

    def test_find_watchers_by_work_package(self):
        self.assertNotNull(self.wpSer.find_watchers_by_work_package(self.work_package))

    def test_create_watcher(self):
        self.assertNotNull(self.wpSer.create_watcher(self.work_package, watcher))

    def test_delete_watcher(self):
        self.assertNotNull(self.wpSer.delete_watcher(self.work_package, watcher))

    def test_find_relation_candidates_by_work_package(self):
        self.assertNotNull(self.wpSer.find_relation_candidates_by_work_package(self.work_package, filters, query, type, pageSize))

    def test_find_available_watchers_by_work_package(self):
        self.assertNotNull(self.wpSer.find_available_watchers_by_work_package(self.work_package))

    def test_find_available_projects_by_work_package(self):
        self.assertNotNull(self.wpSer.find_available_projects_by_work_package(self.work_package))

    def test_find_revisions_by_work_package(self, work_package):
        self.assertNotNull(self.wpSer.find_revisions_by_work_package(self.work_package))

    def test_find_activities_by_work_package(self):
        self.assertNotNull(self.wpSer.find_activities_by_work_package(self.work_package, notify))

    def test_create_activity(self):
        self.assertNotNull(self.wpSer.create_activity(self.work_package, activity, notify))
