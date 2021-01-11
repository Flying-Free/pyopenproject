import unittest

from business.wiki_page_service import WikiPageService


class WikiPageServiceTestCase(unittest.TestCase):
    wikiPageSer = WikiPageService()

    def find(self):
        self.assertNotNull(self.wikiPageSer.find(wiki_page))

    def find_attachments(self):
        self.assertNotNull(self.wikiPageSer.find(context, identifier, body))

    def add_attachment(self):
        self.assertNotNull(self.wikiPageSer.add_attachment(context, identifier, body))
