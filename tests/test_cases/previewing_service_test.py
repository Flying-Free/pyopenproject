from tests.test_cases.openproject_test_case import OpenProjectTestCase


class RenderServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.previewingSer = self.factory.get_previewing_service()

    def test_to_markdown(self):
        current = self.previewingSer.from_markdown(text='Hello world! "This":http://example.com **is** markdown')
        self.assertEqual('<p class="op-uc-p">Hello world! "This":'
                         '<a href="http://example.com" class="op-uc-link">http://example.com</a>'
                         ' <strong>is</strong> markdown</p>'
                         , current)

    def test_to_markdown_by_context(self):
        # Supported contexts:
        #
        # /api/v3/work_packages/{id} - an existing work package
        # TODO: We need to review this request. It returns an empty string
        current = self.previewingSer.from_markdown_by_context(context="/api/v3/work_packages/3")
        print(current)
        self.assertIsNotNone(current)

    def test_to_plain(self):
        current = self.previewingSer.from_plain(text="Hello world! This *is* plain text!")
        self.assertEqual("<p>Hello world! This *is* plain text!</p>", current)
