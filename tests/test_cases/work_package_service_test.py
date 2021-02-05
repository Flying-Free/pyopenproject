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
            #     self.activity = WorkPackage(json.load(f))
            # with open('../data/schema.json') as f:
            self.schema = WorkPackage(json.load(f))
        with open(ATTACHMENT) as f:
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
        s = self.wpSer.delete(self.work_package)
        print(s)

    # TODO
    # def test_find_schema(self):
    #     self.assertIsNotNone(self.wpSer.find_schema(self.schema))

    def test_find_all_schemas(self):
        self.assertIsNotNone(self.wpSer.find_all_schemas([Filter("id", "=", ["12-1", "14-2"])]))

    def test_update_work_package_form(self):
        self.assertIsNotNone(self.wpSer.update_work_package(self.work_package))

    def test_find_all(self):
        # TODO: Improve how pass two or more values to a filter
        work_packages = self.wpSer.find_all(25, 25, [Filter("type_id", "=", ["1", "2"])],
                                            '[["status", "asc"]]', "status", True)
        self.assertEqual(0, len(work_packages))

    def test_create(self):
        # FIXME api_connection.exceptions.request_exception.RequestError: Error running request with the URL (HTTPError): 'http://127.0.0.1:8080/api/v3/work_packages/?notify=False'.
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:MultipleErrors",
        #  "message":"Multiple field constraints have been violated.",
        #  "_embedded":{
        #  "errors":[
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyConstraintViolation",
        #  "message":"Assignee The chosen user is not allowed to be 'Assignee' for this work package.",
        #  "_embedded":{
        #  "details":{
        #  "attribute":"assignee"
        #  }
        #  }
        #  },
        #  {"_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyConstraintViolation",
        #  "message":"Accountable The chosen user is not allowed to be 'Accountable' for this work package.",
        #  "_embedded":{
        #  "details":{
        #  "attribute":"responsible"
        #  }
        #  }
        #  },
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyConstraintViolation",
        #  "message":"Parent does not exist.",
        #  "_embedded":{
        #  "details":{
        #  "attribute":"parent"
        #  }
        #  }
        #  },
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyConstraintViolation",
        #  "message":"Category The specified category does not exist.",
        #  "_embedded":{
        #  "details":{
        #  "attribute":"category"
        #  }
        #  }
        #  },
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyConstraintViolation",
        #  "message":"Author is invalid.",
        #  "_embedded":
        #  {
        #  "details":{
        #         "attribute":"author"}}},{"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyIsReadOnly","message":"Author was attempted to be written but is not writable.","_embedded":{
        #         "details":{
        #         "attribute":"author"}}},{"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyIsReadOnly","message":"ID was attempted to be written but is not writable.","_embedded":{
        #         "details":{
        #         "attribute":"id"}}},{"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyIsReadOnly","message":"Created on was attempted to be written but is not writable.","_embedded":{
        #         "details":{
        #         "attribute":"createdAt"}}},{"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyIsReadOnly","message":"Updated on was attempted to be written but is not writable.","_embedded":{
        #         "details":{
        #         "attribute":"updatedAt"}}},{"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:PropertyIsReadOnly","message":"Derived estimated hours was attempted to be written but is not writable.","_embedded":{
        #         "details":{
        #         "attribute":"derivedEstimatedHours"}}}]}}
        wP = WorkPackage(self.wpSer.create_form()._embedded["payload"])
        wP.subject = "Demo task created by the API"
        project = self.wpSer.find_available_projects()[0].__dict__['_links']['self']
        wP._links["project"]["href"] = project['href']
        work_package_type = list(filter(
            lambda x: x.name == 'Task',
            self.factory.get_type_service().find_all()
        ))[0].__dict__['_links']['self']['href']
        wP.__dict__["_links"]["type"]["href"] = work_package_type
        # Without notify
        print(wP.__dict__)
        wP = self.wpSer.create(wP)
        wP = self.wpSer.find(wP)
        # With notify to false
        self.assertIsNotNone(self.wpSer.create(self.work_package, False))

    def test_create_form(self):
        form = self.wpSer.create_form()
        self.assertEqual(self.work_package_form.__dict__, form.__dict__)

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
                            [Filter("status_id", "o", ["null"])], "rollout", "follows", 25)
        self.assertEqual(0, len(relations))

    def test_find_available_watchers(self):
        self.assertIsNotNone(self.wpSer.find_available_watchers(self.work_package))

    # TODO with parameter and without it
    def test_find_available_projects(self):
        self.assertIsNotNone(self.wpSer.find_available_projects(self.work_package))

    def test_find_revisions(self):
        self.assertIsNotNone(self.wpSer.find_revisions(self.work_package))

    def test_find_activities(self):
        self.assertIsNotNone(self.wpSer.find_activities(self.work_package))

    def test_create_activity(self):
        self.assertIsNotNone(self.wpSer.create_activity(self.work_package, self.activity))
        self.assertIsNotNone(self.wpSer.create_activity(self.work_package, self.activity, False))
