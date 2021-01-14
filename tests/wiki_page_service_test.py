import json
import unittest

from business.services.wiki_page_service import WikiPageService


class WikiPageServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.wikiPageSer = WikiPageService()
        self.wiki = json.loads('/data/wiki.json')

    def test_find(self):
        self.assertNotNull(self.wikiPageSer.find(self.wiki))

    def test_find_attachments(self):
        self.assertNotNull(self.wikiPageSer.find(context, identifier, body))

    def test_add_attachment(self):
        self.assertNotNull(self.wikiPageSer.add_attachment(context, identifier, body))
