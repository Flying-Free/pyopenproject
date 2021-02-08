import json
import os

from business.exception.business_error import BusinessError
from model.form import Form
from model.user import User
from model.work_package import WorkPackage
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class WorkPackageServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        WORK_PACKAGE = os.path.join(self.TEST_CASES, '../data/work_package.json')
        WORK_PACKAGE_FORM = os.path.join(self.TEST_CASES, '../data/work_package_form.json')
        RELATION = os.path.join(self.TEST_CASES, '../data/relation.json')
        USER = os.path.join(self.TEST_CASES, '../data/user.json')
        ACTIVITY = os.path.join(self.TEST_CASES, '../data/activity.json')
        ATTACHMENT = os.path.join(self.TEST_CASES, '../data/attachment.json')
        self.wpSer = self.factory.get_work_package_service()
        with open(WORK_PACKAGE) as f:
            self.work_package = WorkPackage(json.load(f))
        with open(WORK_PACKAGE_FORM) as f:
            self.work_package_form = Form(json.load(f))
        with open(RELATION) as f:
            self.relation = WorkPackage(json.load(f))
        with open(USER) as f:
            self.watcher = User(json.load(f))
        with open(ACTIVITY) as f:
            self.activity = WorkPackage(json.load(f))
        # with open('../data/schema.json') as f:
        #     self.schema = WorkPackage(json.load(f))
        with open(ATTACHMENT) as f:
            self.attachment = WorkPackage(json.load(f))

    # TODO
    def test_attachments(self):
        self.wpSer.add_attachment(self.work_package, self.attachment)
        self.assertIsNotNone(self.wpSer.find_attachments(self.work_package))

    def test_not_found(self):
        # There's no activity --> Exception
        with self.assertRaises(BusinessError):
            self.wpSer.find(self.work_package)

    def test_find(self):
        wP = self.new_work_package()
        wP = self.wpSer.create(wP)
        new_wP = self.wpSer.find(wP)
        # Work Package Found
        self.assertEqual(wP.subject, new_wP.subject)
        self.wpSer.delete(wP)

    # FIXME
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:UpdateConflict",
    #  "message":"Could not update the resource because of conflicting modifications."
    #  }
    def test_update(self):
        work_packages = self.wpSer.find_all()
        work_packages = list(filter(lambda x: x.subject == "Set date and location of conference", work_packages))
        work_package = WorkPackage({"id": work_packages[0].id})
        work_package.subject = "Changed subject"
        changed_wP = self.wpSer.update(work_package)
        self.assertEqual(work_package.id, changed_wP.id)
        self.assertEqual(work_package.subject, changed_wP.subject)
        work_package.subject = work_packages[0].subject
        changed_wP = self.wpSer.update(work_package)
        self.assertEqual(work_package.id, changed_wP.id)
        self.assertEqual(work_package.subject, changed_wP.subject)

    def test_delete(self):
        wP = self.new_work_package()
        wP = self.wpSer.create(wP)
        self.wpSer.delete(wP)
        with self.assertRaises(BusinessError):
            self.wpSer.find(wP)

    # TODO
    def test_find_schema(self):
        self.assertIsNotNone(self.wpSer.find_schema(self.schema))

    def test_find_all_schemas(self):
        self.assertIsNotNone(self.wpSer.find_all_schemas([Filter("id", "=", ["12-1", "14-2"])]))

    def test_update_work_package_form(self):
        self.assertIsNotNone(self.wpSer.update_work_package(self.work_package))

    def test_find_all(self):
        work_packages = self.wpSer.find_all(25, 25, [Filter("type_id", "=", ["1", "2"])],
                                            '[["status", "asc"]]', "status", True)
        self.assertEqual(0, len(work_packages))

    def test_create(self):
        wP = self.new_work_package()
        # Without notify
        new_wP = self.wpSer.create(wP)
        new_wP = self.wpSer.find(new_wP)
        self.assertEqual(wP.subject, new_wP.subject)
        self.wpSer.delete(wP)

    def new_work_package(self):
        wP = WorkPackage(self.wpSer.create_form()._embedded["payload"])
        wP.subject = "Demo task created by the API"
        project = self.wpSer.find_available_projects()[0].__dict__['_links']['self']
        wP._links["project"]["href"] = project['href']
        work_package_type = list(filter(
            lambda x: x.name == 'Task',
            self.factory.get_type_service().find_all()
        ))[0].__dict__['_links']['self']['href']
        wP.__dict__["_links"]["type"]["href"] = work_package_type
        return wP

    def test_create_form(self):
        form = self.wpSer.create_form()
        self.assertEqual(self.work_package_form.__dict__, form.__dict__)

    def test_create_relation(self):
        work_packages = self.wpSer.find_all()
        work_packages = list(filter(lambda x: x.__dict__["_links"]["status"]["title"] == "New", work_packages))
        f = work_packages[0]
        t = work_packages[1]
        relation = self.wpSer.create_relation(
            type="follows",
            work_package_from=f,
            work_package_to=t,
            description="Demo relation created using the API")
        self.assertEqual("Demo relation created using the API", relation.description)
        self.assertEqual("follows", relation.type)
        self.assertEqual("precedes", relation.reverseType)
        self.factory.get_relation_service().delete(relation)

    # TODO
    def test_find_relations(self):
        self.assertIsNotNone(self.wpSer.find_relations(self.work_package))

    def test_create_relation_form(self):
        form = self.wpSer.create_relation_form()

    # TODO
    def test_find_watchers(self):
        self.assertIsNotNone(self.wpSer.find_watchers(self.work_package))

    # TODO
    def test_create_watcher(self):
        self.assertIsNotNone(self.wpSer.create_watcher(self.work_package, self.watcher))

    # TODO
    def test_delete_watcher(self):
        self.assertIsNotNone(self.wpSer.delete_watcher(self.work_package, self.watcher))

    # TODO
    def test_find_relation_candidates(self):
        relations=self.wpSer.find_relation_candidates(self.work_package,
                            [Filter("status_id", "o", ["null"])], "rollout", "follows", 25)
        self.assertEqual(0, len(relations))

    # TODO
    def test_find_available_watchers(self):
        self.assertIsNotNone(self.wpSer.find_available_watchers(self.work_package))

    # TODO with parameter and without it
    def test_find_available_projects(self):
        self.assertIsNotNone(self.wpSer.find_available_projects(self.work_package))

    # TODO
    def test_find_revisions(self):
        self.assertIsNotNone(self.wpSer.find_revisions(self.work_package))

    # TODO
    def test_find_activities(self):
        self.assertIsNotNone(self.wpSer.find_activities(self.work_package))

    # TODO
    def test_create_activity(self):
        self.assertIsNotNone(self.wpSer.create_activity(self.work_package, self.activity))
        self.assertIsNotNone(self.wpSer.create_activity(self.work_package, self.activity, False))
