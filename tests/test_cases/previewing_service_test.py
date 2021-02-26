from tests.test_cases.openproject_test_case import OpenProjectTestCase


class PreviewingServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.previewingSer = self.op.get_previewing_service()

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
        # TODO We don't know what is the difference between this and with no additional context

        r = self.previewingSer.from_markdown(
            text='Hello world! "This":http://example.com **is** markdown',
            context="/api/v3/work_packages/3")
        self.assertIsNot('Hello world! "This":http://example.com **is** markdown', r)

    def test_to_plain(self):
        current = self.previewingSer.from_plain(text="Hello world! This *is* plain text!")
        self.assertEqual("<p>Hello world! This *is* plain text!</p>", current)
