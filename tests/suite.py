import unittest

from tests.test_cases.activity_service_test import ActivityServiceTestCase
from tests.test_cases.attachment_service_test import AttachmentServiceTestCase
from tests.test_cases.budget_service_test import BudgetServiceTestCase
from tests.test_cases.category_service_test import CategoryServiceTestCase
from tests.test_cases.configuration_service_test import ConfigurationServiceTestCase
from tests.test_cases.custom_action_service_test import CustomActionServiceTestCase
from tests.test_cases.custom_object_service_test import CustomObjectServiceTestCase
from tests.test_cases.document_service_test import DocumentServiceTestCase
from tests.test_cases.grid_service_test import GridServiceTestCase
from tests.test_cases.group_service_test import GroupServiceTestCase
from tests.test_cases.help_texts_service_test import HelpTextsServiceTestCase
from tests.test_cases.membership_service_test import MembershipServiceTestCase
from tests.test_cases.news_service_test import NewsServiceTestCase
from tests.test_cases.post_service_test import PostServiceTestCase
from tests.test_cases.previewing_service_test import PreviewingServiceTestCase
from tests.test_cases.principal_service_test import PrincipalServiceTestCase
from tests.test_cases.priority_service_test import PriorityServiceTestCase
from tests.test_cases.project_service_test import ProjectServiceTestCase
from tests.test_cases.query_service_test import QueryServiceTestCase
from tests.test_cases.relation_service_test import RelationServiceTestCase
from tests.test_cases.revision_service_test import RevisionServiceTestCase
from tests.test_cases.role_service_test import RoleServiceTestCase
from tests.test_cases.root_service_test import RootServiceTestCase
from tests.test_cases.schema_service_test import SchemaServiceTestCase
from tests.test_cases.status_service_test import StatusServiceTestCase
from tests.test_cases.time_entry_service_test import TimeEntryServiceTestCase
from tests.test_cases.type_service_test import TypeServiceTestCase
from tests.test_cases.user_service_test import UserServiceTestCase
from tests.test_cases.version_service_test import VersionServiceTestCase
from tests.test_cases.wiki_page_service_test import WikiPageServiceTestCase
from tests.test_cases.work_package_service_test import WorkPackageServiceTestCase


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ActivityServiceTestCase))
    test_suite.addTest(unittest.makeSuite(AttachmentServiceTestCase))
    test_suite.addTest(unittest.makeSuite(BudgetServiceTestCase))
    test_suite.addTest(unittest.makeSuite(CategoryServiceTestCase))
    test_suite.addTest(unittest.makeSuite(ConfigurationServiceTestCase))
    test_suite.addTest(unittest.makeSuite(CustomActionServiceTestCase))
    test_suite.addTest(unittest.makeSuite(CustomObjectServiceTestCase))
    test_suite.addTest(unittest.makeSuite(DocumentServiceTestCase))
    test_suite.addTest(unittest.makeSuite(GridServiceTestCase))
    test_suite.addTest(unittest.makeSuite(GroupServiceTestCase))
    test_suite.addTest(unittest.makeSuite(HelpTextsServiceTestCase))
    test_suite.addTest(unittest.makeSuite(MembershipServiceTestCase))
    test_suite.addTest(unittest.makeSuite(NewsServiceTestCase))
    test_suite.addTest(unittest.makeSuite(PostServiceTestCase))
    test_suite.addTest(unittest.makeSuite(PreviewingServiceTestCase))
    test_suite.addTest(unittest.makeSuite(PrincipalServiceTestCase))
    test_suite.addTest(unittest.makeSuite(PriorityServiceTestCase))
    test_suite.addTest(unittest.makeSuite(ProjectServiceTestCase))
    test_suite.addTest(unittest.makeSuite(QueryServiceTestCase))
    test_suite.addTest(unittest.makeSuite(RelationServiceTestCase))
    test_suite.addTest(unittest.makeSuite(RevisionServiceTestCase))
    test_suite.addTest(unittest.makeSuite(RoleServiceTestCase))
    test_suite.addTest(unittest.makeSuite(RootServiceTestCase))
    test_suite.addTest(unittest.makeSuite(SchemaServiceTestCase))
    test_suite.addTest(unittest.makeSuite(StatusServiceTestCase))
    test_suite.addTest(unittest.makeSuite(TimeEntryServiceTestCase))
    test_suite.addTest(unittest.makeSuite(TypeServiceTestCase))
    test_suite.addTest(unittest.makeSuite(UserServiceTestCase))
    test_suite.addTest(unittest.makeSuite(VersionServiceTestCase))
    test_suite.addTest(unittest.makeSuite(WikiPageServiceTestCase))
    test_suite.addTest(unittest.makeSuite(WorkPackageServiceTestCase))
    return test_suite


if __name__ == '__main__':
    mySuit = suite()
    runner = unittest.TextTestRunner()
    runner.run(mySuit)
