import json

from business.services.wiki_page_service import WikiPageService
from model.wiki_page import WikiPage


class WikiPageServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.wikiPageSer = WikiPageService()
        with open('../data/work_package.json') as f:
            self.wiki = WikiPage(json.load(f))
        with open('../data/attachment.json') as f:
            self.attachment = WikiPage(json.load(f))

    def test_find(self):
        self.assertIsNotNone(self.wikiPageSer.find(self.wiki))

    def test_find_attachments(self):
        self.assertIsNotNone(self.wikiPageSer.find_attachments(self.wiki))

    def test_add_attachment(self):
        self.assertIsNotNone(self.wikiPageSer.add_attachment(self.wiki, self.attachment))
