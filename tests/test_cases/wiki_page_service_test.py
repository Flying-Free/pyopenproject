import json
import os

from business.exception.business_error import BusinessError
from model.wiki_page import WikiPage
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class WikiPageServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/work_package.json')
        ATTACHMENT = os.path.join(self.TEST_CASES, '../data/attachment.json')
        self.wikiPageSer = self.factory.get_wiki_page_service()
        with open(DATA) as f:
            self.wiki = WikiPage(json.load(f))
        with open(ATTACHMENT) as f:
            self.attachment = WikiPage(json.load(f))

    def test_find(self):
        # There's no wiki page --> Exception
        with self.assertRaises(BusinessError):
            self.wikiPageSer.find(self.wiki)

    def test_find_attachments(self):
        attachments = self.wikiPageSer.find_attachments(self.wiki)
        self.assertEqual(0, len(attachments))

    def test_add_attachment(self):
        self.assertIsNotNone(self.wikiPageSer.add_attachment(self.wiki, self.attachment))
