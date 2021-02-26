
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RootServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.rootSer = self.op.get_root_service()

    def test_find(self):
        root = self.rootSer.find()
        self.assertIsNotNone(root)
        self.assertEqual(root.instanceName, 'OpenProject')
