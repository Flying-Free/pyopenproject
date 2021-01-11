import unittest

from business.work_package_service import WorkPackageService


class WorkPackageServiceTestCase(unittest.TestCase):
    wpSer = WorkPackageService()

    def test_find_by_context(self, context):
        self.assertNotNull(self.wpSer.find_by_context(context))


    def test_find_attachments(self):
        self.assertNotNull(self.wpSer.find_attachments(work_package))


    def test_add_attachment(self):
        self.assertNotNull(self.wpSer.add_attachment(work_package, attachment))

    def test_find(self):
        self.assertNotNull(self.wpSer.find(notify))

    def test_update_work_package(self):
        self.assertNotNull(self.wpSer.update_work_package(work_package, notify))

    def test_delete_work_package(self):
        self.assertNotNull(self.wpSer.delete_work_package(work_package, notify))

    def test_find_schema(self):
        self.assertNotNull(self.wpSer.find_schema(schema))


    def test_find_all_schemas(self, filters):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_update_work_package_form(self, work_package):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_find_all(self, notify, offset, pageSize,filters, sortBy, groupBy, showSums):
        self.assertNotNull(self.wpSer.find_by_id(1))

    def new_work_package(self, work_package, notify):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_new_work_package_form(self, work_package):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_new_relation(self, work_package, relation):
        self.assertNotNull(self.wpSer.find_by_id(1))

    def test_find_relations_by_work_package(self, work_package):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_new_relation_form(self, relation):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_find_watchers_by_work_package(self, work_package):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_new_watcher(self, work_package, watcher):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_delete_watcher(self, work_package, watcher):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_find_relation_candidates_by_work_package(self, work_package, filters, query, type, pageSize):
        self.assertNotNull(self.wpSer.find_by_id(1))

    def test_find_available_watchers_by_work_package(self, work_package):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_find_available_projects_by_work_package(self, work_package):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_find_revisions_by_work_package(self, work_package):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_find_activities_by_work_package(self, work_package, notify):
        self.assertNotNull(self.wpSer.find_by_id(1))


    def test_new_activity(self, work_package, activity, notify):
        self.assertNotNull(self.wpSer.find_by_id(1))
