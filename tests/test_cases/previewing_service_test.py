from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RenderServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.renderSer = self.factory.get_previewing_service()

    # TODO
    def render_request(self):
        self.assertIsNotNone(self.renderSer.request(1))
