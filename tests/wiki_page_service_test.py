import unittest

from business.wiki_page_service import WikiPageService


class WikiPageServiceTestCase(unittest.TestCase):
    wikiPageSer = WikiPageService()

    def wiki_page_request(self):
        self.assertNotNull(self.wikiPageSer.request(1))
